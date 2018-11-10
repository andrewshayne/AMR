from surprise import BaselineOnly
from surprise import KNNBasic
from surprise import KNNWithMeans
from surprise import KNNWithZScore
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate

from collections import defaultdict
import urllib.request as urlreq
import xmltodict
import csv
import sys
import os

my_username = sys.argv[1]
dataset = os.path.expanduser('anime_db_n.csv')
#dataset = 'anime_db300.csv'

N_ANIME = 10
count = 0
similar_watched = 0.8
user_ratings = {}
anime_list = {}


# function to add user to dataset
def add_to_trainset(my_ratings):
	# check if user is in the set first...
	in_dataset = False
	with open(dataset, 'r', newline='') as datafile:
		reader = csv.reader(datafile)
		for row in reader:
			#print('name:', row[0])
			if(row[0] == my_username):
				in_dataset = True
				break
				
	# add user if not in dataset
	if(not in_dataset):
		print('adding user to dataset')
		with open(dataset, 'a', newline='') as datafile:
			writer = csv.writer(datafile)
			for key in my_ratings:
				writer.writerow([my_username, key, my_ratings[key]])
	else:
		print('user is already in the dataset')
		
		
		
	# check if user is in the id_user first...
	in_id_user = False
	line_num = 1
	with open('id_user.csv', 'r', newline='') as datafile:
		reader = csv.reader(datafile)
		for row in reader:
			line_num += 1
			#print('name:', row[0])
			if(row[1] == my_username):
				in_id_user = True
				break
				
	if(not in_id_user):
		print('adding user to id_user')
		with open('id_user.csv', 'a', newline='') as datafile:
			writer = csv.writer(datafile)
			writer.writerow([line_num, my_username])
	else:
		print('user is already in id_user')
		
		
	print('Putting anime list in dict...')
	with open('anime_list.csv', 'r', newline='', encoding='utf8') as datafile:
		reader = csv.reader(datafile)
		next(reader, None) # skip the headers
		for row in reader:
			# id : (title, rank)
			anime_list[row[2]] = (row[1],row[0])
	

# function to return the ratings from a user
def get_ratings(username):
	user_xml = 'https://myanimelist.net/malappinfo.php?u=' + username + '&status=all&type=anime'
	fp = urlreq.urlopen(user_xml)
	data = fp.read()
	fp.close()

	data = xmltodict.parse(data)
	if(isinstance(data['myanimelist'], type(None))):
		return

	thing = data['myanimelist']['myinfo']['user_completed']
	if(int(thing) < N_ANIME):
		return

	ratings = {}
	count = 0

	for anime in data['myanimelist']['anime']: #if completed
		if(anime['my_status'] == '2'):
			if(int(anime['my_score']) > 0):
				count += 1
				#print(str(count) + '. ' + anime['series_title'] + ' : ' + anime['my_score'])
				ratings[anime['series_animedb_id']] = anime['my_score']

	if(len(ratings) > N_ANIME): #MUST HAVE COMPLETED N_ANIME
		print(len(ratings), '/', thing, '\t', username)

	return ratings
	
	
def get_top_n(predictions, n=10):
	'''
	Returns:
	A dict where keys are user (raw) ids and values are lists of tuples:
		[(raw item id, rating estimation), ...] of size n.
	'''

    # First map the predictions to each user.
	top_n = defaultdict(list)
	for uid, iid, true_r, est, _ in predictions:
		top_n[uid].append((iid, est))

	# Then sort the predictions for each user and retrieve the k highest ones.
	#for uid, user_ratings in top_n.items():
	#    user_ratings.sort(key=lambda x: x[1], reverse=True)
	#    top_n[uid] = user_ratings[:n]
	#
	#return top_n
	print('Getting top results...')
	top_n_user = sorted(top_n[my_username], key=lambda x: x[1], reverse=True)
	top_n_user = top_n_user[:n]
	
	return top_n_user
	
	
##################################?
def read_item_names():
	rid_to_name = {}
	name_to_rid = {}
	with open('id_user.csv', 'r', newline='') as f:
		reader = csv.reader(f)
		for line in reader:
			#print('id: ' + line[0] + ', name: ' + line[1])
			rid_to_name[line[1]] = line[0]
			name_to_rid[line[0]] = line[1]
	
	return rid_to_name, name_to_rid
##################################?


# consider different similarity measures:
	# cosine
	# msd
	# pearson
	# pearson_baseline

if __name__ == '__main__':
	print('username:', my_username)

	user_ratings = get_ratings(my_username)
	#print('ratings:')
	count = 0
	for item in user_ratings:
		count += 1
		#print (str(count) + '. ' + item , ':', user_ratings[item])
		
	add_to_trainset(user_ratings)
	
	reader = Reader(line_format='user item rating',sep=',',rating_scale=(1, 10))
	data = Dataset.load_from_file(dataset, reader=reader)

	#print('BaselineOnly')
	#cross_validate(BaselineOnly(), data, verbose=True)
	#print('KNNBasic')
	#cross_validate(KNNBasic(), data, verbose=True)
	
	trainset = data.build_full_trainset()
	#sim_options = {'name':'cosine','user_based':True,'min_support':(int(round(count * similar_watched)))}
	sim_options = {'name':'cosine','user_based':True,'min_support':10}
	algo = KNNBasic(k=40,min_k=5,sim_options=sim_options)
	#algo = KNNWithMeans(k=40,min_k=5,sim_options=sim_options)
	#algo = KNNWithZScore(k=40,min_k=5,sim_options=sim_options)
	algo.fit(trainset)
	
	
	
	# get a prediction for specific users and items.
	uid = my_username
	iid = str(19) # Monster
	#
	#pred = algo.predict(uid, iid, verbose=True)
	#
	#for x in range (1, 1001):
	#	pred = algo.predict(uid, str(x), verbose=True)
	
	my_dict = {}
	for id in anime_list:
		pred = algo.predict(uid, id, verbose=False)
		if(id not in user_ratings):
			if(pred[4]['was_impossible'] == False):
				#print('id:', pred[1], ':', pred[3], ', k:', pred[4]['actual_k'], pred[4])
				my_dict[id] = pred[3]
	
	
	top_list = sorted(my_dict, key=my_dict.get, reverse=True)[:50]
	for item in top_list:
		print('Rank:\t' + anime_list[item][1], '\t', anime_list[item][0] + ' (' + item + ')', '\t', my_dict[item])
	
	'''	this should print a list of your worst recommendations?
	print('\n WORST')
	worst_list = sorted(my_dict, key=my_dict.get, reverse=False)[:50]
	for item in worst_list:
		if(int(item) < 1000):
			print('Rank:\t' + anime_list[item][1], '\t', anime_list[item][0] + ' (' + item + ')', '\t', my_dict[item])
	'''
	
	#testset = trainset.build_anti_testset()
	#predictions = algo.test(testset)
	#print(get_top_n(predictions, n=10))
	
	
	
	
	
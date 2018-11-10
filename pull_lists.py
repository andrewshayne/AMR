import urllib.request as urlreq
import xmltodict
import re
import csv
import sys
import threading
import time

# CONSTANTS
N_ANIME = 10
my_file = sys.argv[1]
print('filename:', my_file)
url_left = 'https://myanimelist.net/profile/' # change to profile url to get list
url_right = '.php' # ...

mutex = threading.Lock()

# keys
user_count = 0
user_dict = {}

row_count = 0

# function to return the ratings from a user
def get_ratings(username):
	#tmp_count += 1
	user_xml = 'https://myanimelist.net/malappinfo.php?u=' + username + '&status=all&type=anime'
	fp = urlreq.urlopen(user_xml)
	data = fp.read()
	fp.close()
	#print('tmp_count:', tmp_count)
	#continue

	# this gives about 2 pages per second...
	data = xmltodict.parse(data)
	if(isinstance(data['myanimelist'], type(None))):
		return
		#continue

	# MAJOR PROBLEM: SOME PEOPLE HAVE 700+ COMPLETED BUT NO RATINGS!
	# Potential solution: After verifying 1/2 of their shows are not rated, exclude the user?

	# check if completed is at least 10...
	thing = data['myanimelist']['myinfo']['user_completed']
	if(int(thing) < N_ANIME):
		return
		#continue

	ratings = {}
	count = 0

	for anime in data['myanimelist']['anime']: #if completed
		if(anime['my_status'] == '2'):
			if(int(anime['my_score']) > 0):
				count += 1
				# print(str(count) + '. ' + anime['series_title'] + ' : ' + anime['my_score'])
				ratings[anime['series_animedb_id']] = anime['my_score']

	#MUST HAVE COMPLETED and rated N_ANIME
	if(len(ratings) > N_ANIME): #MUST HAVE COMPLETED N_ANIME
		#usr_count += 1
		print(len(ratings), '/', thing, '\t', username)
		for key in ratings:
			mutex.acquire()
			writer.writerow([username, key, ratings[key]])
			mutex.release()

	user_dict[username] = ratings
	#break

def write_count():
	with open ('lines_complete.txt', 'w', newline='') as my_file:
		writer = csv.writer(my_file)
		writer.writerow([str(row_count)])


# END DEFS

delete_count = 0
with open('lines_complete.txt', 'r') as cfile:
	delete_count = int(cfile.readline())

print('delete lines:', delete_count)
with open('sorted_users.csv', 'r') as fin:
	l_data = fin.read().splitlines(True)
with open('sorted_users.csv', 'w') as fout:
	fout.writelines(l_data[delete_count:])



# put each user into dict
with open(my_file, 'r', newline='') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		user_count += 1
		user_dict[''.join(row)] = {}
		# print(user_count, ''.join(row))


# run blocks of threads and wait for all to finish before proceeding to the next block...

with open('anime_db.csv', 'a', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['user', 'anime_id', 'rating'])

	usr_count = 0
	tmp_count = 0

	# try 10 keys at a time...
	keys = list(user_dict.keys())

	index = 0
	blocksize = 10
	while(index < len(keys)):
		row_count += 10
		print('row_count:', row_count)
		write_count()

		threads = []
		for x in range(blocksize):
			t = threading.Thread(target = get_ratings, args=(keys[index + x],))
			threads.append(t)
			t.start()
		# run all 10 requests, wait for them to join...
		for t in threads:
			t.join()

		index += blocksize
		time.sleep(4)
	#for usr in user_dict:
	#	get_ratings(usr)


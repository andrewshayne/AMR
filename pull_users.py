import urllib.request as urlreq
import re
import csv
import time

# CONSTANTS
url = 'https://myanimelist.net/users.php'
left_str = '/profile/'
right_str = '\"><img'

# keys
user_count = 0
user_dict = {}

# begin by reading all existing names into a dict...
with open('users.csv', 'r', newline='') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		user_count += 1
		user_dict[''.join(row)] = ''.join(row)
		print(user_count, ''.join(row))

while True:
	# access current webpage
	fp = urlreq.urlopen(url)
	my_bytes = fp.read()
	html_str = my_bytes.decode('utf8')
	fp.close()

	# get 20 recently online users
	all = re.findall(r'/profile/(.*?)\"><img',html_str)
	print('all: ', all)

	# write names to csv
	with open('users.csv', 'a', newline='') as csvfile:
		writer = csv.writer(csvfile)
		for usr in all:
			# if user is not already in the csv add them to it
			if usr not in user_dict:
				# add them to the dict as well
				user_dict[''.join(usr)] = ''.join(usr)
				# print('added to dict:', ''.join(usr))
				writer.writerow([usr])
			else:
				print('DUPLICATE FOUND:', usr)
	time.sleep(2)
	# break

# For user-anime-list csv:
# | user | rating | anime_id |

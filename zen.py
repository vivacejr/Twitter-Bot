import tweepy	
import time	

print('Please enter the link')

CONSUMER_KEY = 'QJJmBn2z9NB6RDdkSURp5vtV5'
CONSUMER_SECRET = 'O5Mf0X88F8poLxoRDmZssWaHigEwE1G5OQbnpS7ATuib1L3wDq'
ACCESS_KEY = '551845623-XW7VpMrpexZmcgAfaVrf8yx0eYUJkwrMduQqyfDV'
ACCESS_SECRET = 'TU6h6VxzZW0JkjmynhKxtgtMPcC0vJ2aT8DUxMpVz3E1I'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth) 
 
FILE_NAME = 'text_file.txt'


def retrieve_reply(file_name):
	data = []
	f_read = open(file_name, 'r')
	for line in f_read:
		data.append((line.strip()))
	f_read.close()
	data= ''.join(data)
	print(data)
	return data


def get_id(url):
	return url.split('/')[-1]
	
def get_username(url):
	return url.split('/')[-3]


def reply(url):
	id=get_id(url)
	tweet = api.get_status(int(id))
	username = get_username(url)
	print(username)
	print(tweet.text)
	ret = retrieve_reply(FILE_NAME)
	api.update_status('@' + username + ' ' + ret ,id )

url= input()
reply(url)
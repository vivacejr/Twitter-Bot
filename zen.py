import tweepy	
import time	

print('Please enter the link')

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

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

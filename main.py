import tweepy	
import time	

print('ZenBot')

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
	f_read = open(file_name, 'r')
	for line in f_read:
		last_seen_id = int(line.strip())
	f_read.close()
	return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return


CONSUMER_KEY = 'QJJmBn2z9NB6RDdkSURp5vtV5'
CONSUMER_SECRET = 'O5Mf0X88F8poLxoRDmZssWaHigEwE1G5OQbnpS7ATuib1L3wDq'
ACCESS_KEY = '551845623-XW7VpMrpexZmcgAfaVrf8yx0eYUJkwrMduQqyfDV'
ACCESS_SECRET = 'TU6h6VxzZW0JkjmynhKxtgtMPcC0vJ2aT8DUxMpVz3E1I'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth) 

def reply():
	print('Replying')	
	last_seen_id = retrieve_last_seen_id(FILE_NAME)
	mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
	# for status in tweepy.Cursor(api.user_timeline).items():
	# 	try:
	# 		api.destroy_status(status.id)
	# 	except:
	# 		pass
	for mention in reversed(mentions):
	    print(str(mention.id) + ' - ' + mention.full_text, flush=True)
	    last_seen_id = mention.id
	    store_last_seen_id(last_seen_id, FILE_NAME)
	    if '#helloworld' in mention.full_text.lower():
	        print('found #helloworld!', flush=True)
	        print('responding back...', flush=True)
	        api.update_status('@' + mention.user.screen_name +
	                '#HelloWorld back to you!', mention.id)
while(1):
	reply()
	time.sleep(10)
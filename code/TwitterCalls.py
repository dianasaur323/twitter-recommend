# Module of relevant Twitter call functions

from urlparse import urlparse
import urllib
import base64
import requests
import json
import gzip

from DataStructures import TwitterPost


# Global authentication
CONSUMER_KEY = "Xh0V9aWVmLLTPooWv14EkVBLo"
CONSUMER_SECRET = "uoPiycXVTwrXgdR4hHM8hAH5z7rpMZwUdDeKqoy4rp8LOf3XP2"

def authenticate():

	# pre-process keys

	consumerKey = urlparse(CONSUMER_KEY)
	consumerSecret = urlparse(CONSUMER_SECRET)

	combinedAuth = consumerKey[2] + ":" + consumerSecret[2]
	encodedAuth = base64.b64encode(combinedAuth)

	# get bearer token for application only requests

	url = 'https://api.twitter.com/oauth2/token'
	headers = {
		'Authorization': 'Basic {}'.format(encodedAuth),
		'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
		}
	data = 'grant_type=client_credentials'
	response = requests.post(url, headers=headers, data=data)
	response_data = response.json()
	if response_data['token_type'] == 'bearer':
		bearer_token = response_data['access_token']
	else:
		raise RuntimeError('unexpected token type: {}'.format(response_data['token_type']))

	authorizedHeader = {
		'Authorization':'Bearer {}'.format(bearer_token),
		'Accept-Encoding':'gzip',
	}

	return authorizedHeader

def parseTweets(response_data):
	
	returnedTweets=[]

	for doc in response_data:
		twitterPost = TwitterPost(doc['id'])
		twitterPost.set_user((doc['user'])['screen_name'])
		twitterPost.set_user_id((doc['user'])['id'])
		twitterPost.set_retweet(doc['retweet_count'])
		for doc in (doc['entities'])['hashtags']:
			twitterPost.set_hashtags(doc['text'])
		returnedTweets.append(twitterPost)
		# print twitterPost.print_string()
	return returnedTweets
	
def findArticlePosters(url_request):
	# First run authentication to allow Twitter pulls
	authorizedHeader = authenticate()

	# Twitter pulls for tweets containing url
	url = 'https://api.twitter.com/1.1/search/tweets.json'
	params = {'q':url_request}
	response = requests.get(url,headers=authorizedHeader, params=params)
	response_data=response.json()['statuses']

	# Define list that will contain results from Twitter call in the form of TwitterPost instances
	return parseTweets(response_data)

def findTopicSearchPosters(search_text):
	# First run authentication to allow Twitter pulls
	authorizedHeader = authenticate()

	# Twitter pulls for tweets containing url
	url = 'https://api.twitter.com/1.1/search/tweets.json'
	params = {'q':search_text}
	response = requests.get(url,headers=authorizedHeader, params=params)
	response_data=response.json()['statuses']

	# Define list that will contain results from Twitter call in the form of TwitterPost instances
	return parseTweets(response_data)

def userStream(tweets):

	url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

	# First run authentication to allow Twitter pulls
	authorizedHeader = authenticate()

	user_list = []

	# Parse through tweets to get users
	for tweet in tweets:
		user_list.append(tweet.get_user_id())

	# Twitter pulls for tweets related to user
	for user in user_list:
		params = {'user_id':user}
		response = requests.get(url,headers=authorizedHeader,params=params)
		response_data = response.json()
		for doc in response_data:
			for doc in (doc['entities'])['hashtags']:
				print doc['text']

	return user_list

userStream(findArticlePosters('www.newyorker.com'))





#Run tf-idf on Twitter stream

import TwitterCalls
import tfidf

def relevantPosters(users):
	tweetStream = TwitterCalls.userStream(users)

def rankUsers(users):
	tfidf.rankUsers(users)
	return users


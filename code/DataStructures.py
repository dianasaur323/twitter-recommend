# Document contains class definitions of useful data structures

# Twitter post data structure

class TwitterPost (object):
	def __init__ (self,tweet_id):
		self.tweet_id = tweet_id
		self.hashtags = []

	def set_hashtags (self,hashtags):
		self.hashtags.append(hashtags)

	def set_user (self,user_id):
		self.user_id = user_id

	def set_user_id (self,user_id):
		self.user_id_num = user_id

	def get_user_id (self):
		return self.user_id_num

	def set_retweet (self,retweet):
		self.retweet = retweet

	def print_string(self):
		return "tweet_id: " + str(self.tweet_id) + " hashtags: " + str(self.hashtags) + " user: " + str(self.user_id) + " user_id: " + str(self.user_id_num )+ " retweet: " + str(self.retweet)
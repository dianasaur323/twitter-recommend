#Ranks the hashtags of relevant users

import TopicEngine
import TwitterCalls
import math

class tfidf(object):

	def __init__ (self):
		self.doc_num = 0

	# Returns inverse document frequency

	def inc_doc_num (self):
		self.doc_num += 1

	def return_word_list (self,text):

		text = text.replace('.',' ').replace('!', ' ').replace('?', ' ').replace('-', ' ') \
	        .replace('%', ' ').replace("'s"," ").replace('(',' ').replace(')',' ').replace('0', ' ') \
	        .replace('1', ' ').replace('2', ' ').replace('3', ' ').replace('4', ' ') .replace('5', ' ') \
	        .replace('6', ' ').replace('7', ' ').replace('8', ' ').replace('9', ' ').replace('"',' ')

	        #remove duplicates
	        word_list=list(set(text.split()))
		return word_list

	def return_word_dict (self,word_list):
		article_word_dict={}

		for word in word_list:
			if word in article_word_dict.keys():
				article_word_dict[word]=article_word_dict.get(word) + 1
			else:
				article_word_dict[word] = 1
		
		return article_word_dict

	def inv_doc_freq (self,term,doc_num):

		article_word_dict = eval(open('NYT_word_dict.txt','r').read())
		article_count = article_word_dict.get(term)
		
		if article_count != None:
			return math.log(doc_num/article_count)
		else 




	# def rankUsers (tweetStream):
	# 	TwitterCalls.followers(())
	# 	return tweetStream

	# def pullHashTags (tweetStream):
	# 	return tweetStream

	# def runtfidf (hashtags):
	# 	return hashtags

	# def matchTopic (hashtags):
	# 	topic = TopicEngine.matchTopic(hashtags)
	# 	return topic
#Ranks the hashtags of relevant users

import math
import TextParser

class tfidf(object):

	def __init__ (self):
		self.doc_num = 0
		self.word_list = []
		self.word_dict = {}
		self.tfidf_dict = {}
		self.term_freq_dict = {}
		self.word_num = 0
		self.doc_word_list = []

	# Returns inverse document frequency

	def inc_doc_num (self):
		self.doc_num += 1

	def return_article_dict (self,article_list):

		# find unique words

		for doc in list(article_list):
			if doc['lead_paragraph']!=None:
				self.word_list = self.word_list + list(set(TextParser.return_word_list (doc['lead_paragraph'])))
				self.inc_doc_num()

		for word in self.word_list:
			if word in self.word_dict.keys():
				self.word_dict[word] = self.word_dict.get(word) + 1
			else:
				self.word_dict[word] = 1

		# find document word sets

		for doc in list(article_list):
			if doc['lead_paragraph']!=None:
				self.doc_word_list.append(TextParser.return_word_list(doc['lead_paragraph']))
		print self.doc_word_list[1]

	def inv_doc_freq (self,term,doc_num):

		doc_count = self.word_dict.get(term)

		if doc_count != None:
			return math.log(doc_num/doc_count)
		else:
			return None

	def return_term_freq_dict (self,text,tfidf):

		word_list = self.return_word_list(text)

		for word in word_list:
			if word in self.word_dict.keys():
				self.word_dict[word]=self.word_dict.get(word) + 1
				self.word_num += 1
			else:
				self.word_dict[word]=1
				self.word_num += 1

		for word in word_dict:
			self.term_freq_dict[word] = self.word_dict.get(word) * tfidf.tfidf_dict.get(word)

	def return_tfidf_dict (self):
		for key in self.word_dict:
			self.tfidf_dict[key] = self.inv_doc_freq (key,self.doc_num)

#Ranks the hashtags of relevant users

import math
import TextParser

class tfidf(object):

	# Initiates the global variables needed to calculate tf-idf for a body of text
	def __init__ (self):
		self.doc_num = 0
		self.word_list = [] # Words included only one per document
		self.word_dict = {} # Number of documents containing a word
		self.word_list_total = [] # Total list of words
		self.inv_doc_dict = {} # idf dict
		self.word_num = 0
		self.doc_word_list = [] # List of documents made up of list of words

	# Function to count document number
	def inc_doc_num (self):
		self.doc_num += 1

	# Given a list of documents, return a dictionary that counts the number of word occurrences
	def return_doc_dict (self,doc_list):

		# Process to count number of documents containing a given word
		for doc in doc_list:
			if doc!=None:
				parsedText = TextParser.return_word_list(doc)
				self.word_list = self.word_list + list(set(parsedText))
				self.word_list_total = self.word_list_total + parsedText
				self.doc_word_list.append(parsedText)
				self.inc_doc_num() #count number of documents


		for word in self.word_list:
			if word in self.word_dict.keys():
				self.word_dict[word] = self.word_dict.get(word) + 1
			else:
				self.word_dict[word] = 1

		# Store results in text

		text_file = open('word_list.txt','w')
		text_file.write(str(self.word_list))
		text_file = open('word_list_total.txt','w')
		text_file.write(str(self.word_list_total))
		text_file = open('doc_word_list.txt','w')
		text_file.write(str(self.doc_word_list))
		text_file = open('word_dict.txt','w')
		text_file.write(str(self.word_dict))
		
		self.word_num = len(self.word_list_total)

	def inv_doc_freq (self,term,doc_num):

		doc_count = self.word_dict.get(term)

		if doc_count != None:
			return math.log(doc_num/doc_count)
		else:
			return math.log((doc_num + 1)/1) # in situations when td-idf doesn't have the term

		

	def return_inv_doc_dict (self):
		for key in self.word_dict:
			self.inv_doc_dict[key] = self.inv_doc_freq (key,self.doc_num)

		text_file = open('inv_doc_dict.txt','w')
		text_file.write(str(self.inv_doc_dict))


	def return_tfidf_dict (self,doc): # returns tf-idf per document
		tfidf_dict={}
		for word in doc:
			if self.inv_doc_dict.get(word)!=None:
				tfidf = (doc.count(word)/float(len(doc))) * self.inv_doc_dict.get(word)
				if tfidf>0.05:
					tfidf_dict[word] = tfidf
			else:
				inv_doc = self.inv_doc_freq(word,self.doc_num)
				tfidf = (doc.count(word)/float(len(doc))) * inv_doc
				if tfidf>0.05:
					tfidf_dict[word]=(doc.count(word)/float(len(doc))) * inv_doc

		return tfidf_dict

class new_tfidf(tfidf):

	# define additional functions to pull in tf-idf results from text
	def __init__(self):
		self.inv_doc_dict = eval(open('inv_doc_dict.txt','r').read())
		print self.inv_doc_dict
		self.word_dict = eval(open('word_dict.txt','r').read())
		self.doc_num = len(eval(open('doc_word_list.txt','r').read()))












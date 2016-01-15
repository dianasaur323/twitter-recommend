# This is the main interface that defines availability to users.

import TextParser
from TopicEngine import TopicEngine
import PreProcessor
from tfidf import tfidf, new_tfidf
from sys import argv
import TwitterCalls

# Pulls in document training set from NYT
if argv[1] == "NYT":
	PreProcessor.scrapeNYT(argv[2],argv[3])

elif argv[1] == "train":

	# Instantiate tfidf object to run tf-idf on documents
	topic_tfidf = tfidf()

	PreProcessor.preprocessTopicEngine(topic_tfidf,"NYT_articles.txt")
	topic_engine = TopicEngine(topic_tfidf.doc_word_list)

	topic_engine.GibbsSampling()

else:
	url = argv[1]
	text = argv[2]

	# Get processed document as a list of words
	doc = TextParser.return_word_list(text)

	# Run tf-idf on inputted document
	article_tfidf = new_tfidf()
	doc_dict = article_tfidf.return_tfidf_dict(doc)

	# get words associated with topic

	doc_word_list = eval(open("doc_word_list2.txt",'r').read())
	topics = eval(open("topics.txt",'r').read())
	topics_dict = {}

	doc_count = 0
	vocab = list(set(eval(open ('word_list_total.txt','r').read())))

	# Putting words in topic buckets

	for doc in topics:
		word_count = 0
		for word in doc:
			try:
				if word in topics_dict.keys():
					if doc_word_list[word_count][0][doc_count] !=None:
						topics_dict[word]=topics_dict.get(word) + [doc_word_list[word_count][0][doc_count]]
				else:
					if doc_word_list[word_count][0][doc_count]!=None:
						topics_dict[word] = [doc_word_list[word_count][0][doc_count]]
			except IndexError:
				pass
			word_count+=1
		doc_count +=1
	topic = -1

	for key in doc_dict.keys():
		for e in topics_dict.keys():
			if key in topics_dict.get(e):
				topic = e
				break

	if topic < 0:
		print "no relevant articles found"
	else:
		posters = TwitterCalls.findArticlePosters(topics_dict[topic])
		TwitterCalls.userStream(posters)
		print "searched topic: " + str(topics_dict[topic])

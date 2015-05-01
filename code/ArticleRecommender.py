# Main interface for users to interact with

import TextParser
from TopicEngine import TopicEngine
import PreProcessor
from tfidf import tfidf, new_tfidf
from sys import argv

# Pulls in document training set from NYT
if argv[1] == "NYT":
	PreProcessor.scrapeNYT(argv[2],argv[3])

if argv[1] == "train":

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

	article_tfidf = new_tfidf()
	doc = article_tfidf.return_tfidf_dict(doc)

	print doc

	# article_text = unicode(open("article_text.txt",'r').read(),"utf-8")
	# article_tfidf.return_term_freq_dict(article_text,topic_tfidf)

	# print article_tfidf.term_freq_dict


# users = TwitterCalls.findArticlePosters()
# rankedUsers = UserRanking.relevantPosters(users)

# articleLinks = TwitterCalls.findArticleLinks(rankedUsers)
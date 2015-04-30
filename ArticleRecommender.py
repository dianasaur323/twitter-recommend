# Interface for Article Recommender

# import TwitterCalls
import TextParser
import TopicEngine
# import UserRanking
from tfidf import tfidf

#accepts argv from terminal - input should be a web url
from sys import argv

topic_tfidf = tfidf()

if argv[1] == "train":

	# Get a list of text bodies to pass into the tfidf engine, already scraped
	# TopicEngine.scrapeNYT()

	# Format scarped text, already formatted
	# article_text = open("NYT_articles.txt","r").read()
	# TextParser.fixArticleText(article_text)

	# Get a tfidf for pre-processing for topic engine
	TopicEngine.preprocessTopicEngine(topic_tfidf,"NYT_articles.txt")

	TopicEngine.GibbsSampling(topic_tfidf.doc_word_list)

else:

	article_tfidf = tfidf()
	url_input = argv[1]

	article_text = unicode(open("article_text.txt",'r').read(),"utf-8")
	article_tfidf.return_term_freq_dict(article_text,topic_tfidf)

	print article_tfidf.term_freq_dict


# users = TwitterCalls.findArticlePosters()
# rankedUsers = UserRanking.relevantPosters(users)

# articleLinks = TwitterCalls.findArticleLinks(rankedUsers)
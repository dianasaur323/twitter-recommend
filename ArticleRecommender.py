# Interface for Article Recommender

#import needed modules
import TwitterCalls
import TextParser
import TopicEngine
import UserRanking
import tfidf

#accepts argv from terminal - input should be a web url
from sys import argv

if argv == "train":
	# run the training engine that will topic model NYT documents
	topic_tfidf = tfidf()
	scrapeNYT()
	preprocessTopicEngine(topic_tfidf)

else:
	inv_doc_freq("term",1)

# textInput = TextParser.textParserOutput(argv)
# topic = TopicEngine.findTopic(textInput)

# users = TwitterCalls.findArticlePosters()
# rankedUsers = UserRanking.relevantPosters(users)

# articleLinks = TwitterCalls.findArticleLinks(rankedUsers)
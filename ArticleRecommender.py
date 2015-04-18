# Interface for Article Recommender

#import needed modules
import TwitterCalls
import TextParser
import TopicEngine
import UserRanking

#accepts argv from terminal - input should be a web url
from sys import argv

#run topic model on given article

textInput = TextParser.textParserOutput(argv)
topic = TopicEngine.findTopic(textInput)

users = TwitterCalls.findArticlePosters(argv)
rankedUsers = UserRanking.relevantPosters(users)

articleLinks = TwitterCalls.findArticleLinks(rankedUsers)

#run topic model on given article


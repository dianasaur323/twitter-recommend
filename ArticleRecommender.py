# Interface for Article Recommender

#import needed modules
import TwitterCalls

#accepts argv from terminal - input should be a web url
from sys import argv

TwitterCalls.findArticlePosters(argv)


print argv

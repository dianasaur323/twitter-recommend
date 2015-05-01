# Takes in a url and pulls in the body text and returns a dict

# from html.parser import HTMLParser
# import urllib2

import requests

def return_word_list (text):

	text = text.replace('.',' ').replace('!', ' ').replace('?', ' ').replace('-', ' ') \
		.replace('%', ' ').replace("'s"," ").replace('(',' ').replace(')',' ').replace('0', ' ') \
		.replace('1', ' ').replace('2', ' ').replace('3', ' ').replace('4', ' ') .replace('5', ' ') \
		.replace('6', ' ').replace('7', ' ').replace('8', ' ').replace('9', ' ').replace('"',' ') \
		.replace(u'\u201d', ' ').replace(u'\u201c', ' ').replace(u'\u2014',' ').replace(u'\u2019',' ') \
		.replace("<br/>", ' ').replace('&',' ').replace('#',' ').replace('<',' ').replace('>',' ') \
		.replace("<br>", ' ') 

	#remove duplicates
	word_list=text.split()

	return word_list

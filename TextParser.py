# Takes in a url and pulls in the body text and returns a dict

# from html.parser import HTMLParser
# import urllib2

import requests

def getBodyText (url):

	html = requests.get(url)
	print html.text

	# try:
	# 	response = urllib2.urlopen(url)
	# 	html = response.read()

	# 	parser = HTMLParser()
	# 	parser.feed(html)
	# 	parser.handle_starttag('body')
	# 	print parser.handle_data

	# except urllib2.HTTPError, e:
	# 	print "URL pull error"

# getBodyText('http://techcrunch.com/2015/04/25/the-marijuana-industry-and-its-first-crossroads/#.m3hlzq:aTae')

def return_word_list (text):

	text = text.replace('.',' ').replace('!', ' ').replace('?', ' ').replace('-', ' ') \
        .replace('%', ' ').replace("'s"," ").replace('(',' ').replace(')',' ').replace('0', ' ') \
        .replace('1', ' ').replace('2', ' ').replace('3', ' ').replace('4', ' ') .replace('5', ' ') \
        .replace('6', ' ').replace('7', ' ').replace('8', ' ').replace('9', ' ').replace('"',' ') \
        .replace(u'\u201d', ' ').replace(u'\u201c', ' ').replace(u'\u2014',' ').replace(u'\u2019',' ')

        #remove duplicates
        word_list=text.split()

	return word_list

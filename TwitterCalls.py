# Module of relevant Twitter call functions

from urlparse import urlparse
import urllib
import httplib
import base64
import requests

def authenticate():
	consumerKey = "Xh0V9aWVmLLTPooWv14EkVBLo"
	consumerSecret = "uoPiycXVTwrXgdR4hHM8hAH5z7rpMZwUdDeKqoy4rp8LOf3XP2"

	consumerKey = urlparse(consumerKey)
	consumerSecret = urlparse(consumerSecret)

	combinedAuth = consumerKey[2] + ":" + consumerSecret[2]
	encodedAuth = base64.b64encode(combinedAuth)

	host = 'api.twitter.com'
	url = '/oauth2/token/'

	header = {'Host':host,'User-Agent':'My Twitter 1.1','Authorization':'Basic %s' % encodedAuth,
	'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','Content-Length':'29',
	'Accept-Encoding':'gzip'}

	param='{grant_type:client_credentials}'

	# r=requests.post('http://api.twitter.com/oauth2/token',headers=header,params=param)
	# print r.status_code
	params = urllib.urlencode({'grant_type' : 'client_credentials'})
	req = httplib.HTTPSConnection(host)
	req.putrequest("POST", url)
	req.putheader("Host", host)
	req.putheader("User-Agent", "My Twitter 1.1")
	req.putheader("Authorization", "Basic %s" % encodedAuth)
	req.putheader("Content-Type" ,"application/x-www-form-urlencoded;charset=UTF-8")
	req.putheader("Content-Length", "29")
	req.putheader("Accept-Encoding", "gzip")
	req.endheaders()
	req.send(params)

	resp = req.getresponse()
	print resp.read()

	# 	print 'oauth error', e
	
def findArticlePosters(url):
	authenticate()
	return url

def userStream(users):
	return users

def followers(users):
	return users

def findArticleLinks(rankedUsers):
	return rankedUsers



# Module of relevant Twitter call functions

from urlparse import urlparse
import urllib
import urllib2
import httplib
import base64
import requests
import twitter

def authenticate():
	CONSUMER_KEY = "Xh0V9aWVmLLTPooWv14EkVBLo"
	CONSUMER_SECRET = "uoPiycXVTwrXgdR4hHM8hAH5z7rpMZwUdDeKqoy4rp8LOf3XP2"
	# accessTokenKey = "1648117658-UzlogTNYnYPkHkskdRea5fRn7wc9ikIgP321RVi"
	# accessTokenSecret = "C5LlHEcsZcWJJdhcDKSgQD0Mq36NcdqT0PABurMx2VzS6"

	consumerKey = urlparse(CONSUMER_KEY)
	consumerSecret = urlparse(CONSUMER_SECRET)

	combinedAuth = consumerKey[2] + ":" + consumerSecret[2]
	encodedAuth = base64.b64encode(combinedAuth)

	# host = 'api.twitter.com'
	# url = '/oauth2/token/'



	# params = urllib.urlencode({'grant_type' : 'client_credentials'})
	# req = httplib.HTTPSConnection(host)
	# req.putrequest("POST", url)
	# req.putheader("Host", host)
	# req.putheader("User-Agent", "My Twitter 1.1")
	# req.putheader("Authorization", "Basic %s" % encodedAuth)
	# req.putheader("Content-Type" ,"application/x-www-form-urlencoded;charset=UTF-8")
	# req.putheader("Content-Length", "29")
	# req.putheader("Accept-Encoding", "gzip")
	# req.endheaders()
	# req.send(params)

	# resp = req.getresponse()
	# response = resp.json()
	# print resp.status,resp.reason, response

	# param = 'grant_type=client_credentials'

	# header = {'Post':url,'Host':host,'User-Agent':'My Twitter 1.1','Authorization':'Basic %s' % encodedAuth,
	# 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','Content-Length':'29',
	# 'Accept-Encoding':'gzip'}
	# r=requests.post('http://api.twitter.com/oauth2/token',headers=header,params=param)
	# print r.status_code

	# get bearer token for application only requests

	url = 'https://api.twitter.com/oauth2/token'
	headers = {
	    'Authorization': 'Basic {}'.format(encodedAuth),
	    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
		}
	data = 'grant_type=client_credentials'
	response = requests.post(url, headers=headers, data=data)
	response_data = response.json()
	if response_data['token_type'] == 'bearer':
	    bearer_token = response_data['access_token']
	    print response.status_code
	else:
	    raise RuntimeError('unexpected token type: {}'.format(response_data['token_type']))


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

authenticate()



# TopicEngine implements the latent  dirichlet allocation as described
# in Blei et al. (2003) using collapsed Gibbs Sampling described in 
# Griffiths and Steyvers (2004).

import requests
import json


def scrapeNYT ():

    # New York Times API does not require encoding
    
    url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?'
    api_key = '13bc65215e7fbc5d2ca01f022ee68cf7:1:67898892'
    search_date = 20150415
    date_range = 10

    # New York Times API limits API return calls to 10 results per call and up to 100 page flips.
    # Strategy is to take the total number of articles found in one day, rip through 100 pages, 
    # then move onto the next day for a given range.

    # Good way to iterate through dates? Convert JSON to dict? Parsing through JSON?

    article_list = []

    while date_range > 0:

        #iterate through page numbers
        for i in range(1,2): #change to 100 when ready
            response = requests.get(url+'&begin_date='+str(search_date)+'&end_date='+
                str(search_date)+'&fl=lead_paragraph'+'&page='+str(i)+'&api-key='+api_key)
            response_data = response.json()

            #check if no results found
            hit_count = response_data['response']['meta']['hits']
            if response_data['response']['meta']['hits'] == 0:
                break
            else:
                article_text=response_data['response']['docs']
                article_list.append(article_text)

        #iterate through dates
        date_range -=1 
        search_date -=1

    # Print result to text file
    text_file = open('NYT_articles.txt','a')
    text_file.write(str(article_list))


# Will return article_list as a dict with word occurrence count across the corpus
def preprocessTopicEngine (topic_tfidf):

    #dict that stores each word and the number of occurrences

    article_list = eval(open('NYT_articles.txt','r').read())
    word_list = []

    for doc in article_list:
        # I know this is ugly - will fix
        doc_text = str(doc[0]['lead_paragraph'])
        if doc_text != "None":
            word_list = word_list + topic_tfidf.return_word_list (doc_text)
            topic_tfidf.inc_doc_num()

    # Print result to text file
    article_word_dict = topic_tfidf.return_word_dict(word_list)
    text_file = open('NYT_word_dict.txt','w')
    text_file.write(str(article_word_dict))

def trainTopicEngine (article_list):

	return args

def findTopic (textInput):
	return textInput

def matchTopic (hashtags):
	return hashtags


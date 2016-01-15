import requests
import json
import numpy
import TextParser
import random
import datetime

# scrapeNYT takes New York Times articles and prepares it for tf-idf  by create a list of 
# article text that represent specific documents and stores this in a text file.

def scrapeNYT (begin_date,length):

    # New York Times API does not require encoding
    
    url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?'
    api_key = '13bc65215e7fbc5d2ca01f022ee68cf7:1:67898892'
    search_date = begin_date # current date range: 3/15 - 4/15
    date_range = int(length)

    # New York Times API limits API return calls to 10 results per call and up to 100 page flips.
    # Strategy is to take the total number of articles found in one day, rip through 100 pages, 
    # then move onto the next day for a given range.

    article_list = []

    while date_range > 0:

        #iterate through page numbers
        for i in range(1,5): 
            response = requests.get(url+'&begin_date='+str(search_date)+'&end_date='+
                str(search_date)+'&fl=lead_paragraph'+'&page='+str(i)+'&api-key='+api_key)
            response_data = response.json()

            #check if no results found
            hit_count = response_data['response']['meta']['hits']
            if response_data['response']['meta']['hits'] == 0:
                break
            else:
                for doc in response_data['response']['docs']:
                    article_text = doc['lead_paragraph']
                    if article_text != None:
                        article_list.append(article_text)

        #iterate through dates
        date_range -=1 
        new_date = datetime.date(int(begin_date[0:4]),int(begin_date[4:6]),int(begin_date[6:8])) + datetime.timedelta(days=1)

        #reformat date for NYT API
        if new_date.month < 10:
            month = "0" + str(new_date.month)
        else: 
            month = str(new_date.month)
        if new_date.day < 10:
            day = "0" + str(new_date.day)
        else: 
            day = str(new_date.day)
        search_date = str(new_date.year) + month + day

    # Print result to text file
    text_file = open('NYT_articles.txt','w')
    text_file.write(str(article_list))

# preprocessTopicEngine takes in the name to a text file that contains article text

def preprocessTopicEngine (topic_tfidf,text_file):

    print "preprocessing...."

    doc_list = eval(open(text_file,'r').read())
    topic_tfidf.return_doc_dict(doc_list)
    print "returned document dict"
    topic_tfidf.return_inv_doc_dict()
    print "calculated return_inv_doc"

    # Initialize tfidf_dict as a list to store document tf-idf dict values.
    # Excludes terms with low tf-idf

    tfidf_doc_list=[]
    for doc in topic_tfidf.doc_word_list:
        tfidf_doc_list.append(topic_tfidf.return_tfidf_dict(doc))

    print "returned tfidf"

    text_file = open('NYT_tfidf.txt','w')
    text_file.write(str(tfidf_doc_list))
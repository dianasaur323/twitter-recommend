# TopicEngine implements the latent  dirichlet allocation as described
# in Blei et al. (2003) using collapsed Gibbs Sampling described in 
# Griffiths and Steyvers (2004).

import requests
import json
import numpy
import TextParser
import random

# scrapeNYT takes New York Times articles and prepares it for tf-idf  by create a list of 
# article text that represent specific documents and stores this in a text file.

def scrapeNYT ():

    # New York Times API does not require encoding
    
    url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?'
    api_key = '13bc65215e7fbc5d2ca01f022ee68cf7:1:67898892'
    search_date = 20150412 # date range: 3/15 - 4/12
    date_range = 1

    # New York Times API limits API return calls to 10 results per call and up to 100 page flips.
    # Strategy is to take the total number of articles found in one day, rip through 100 pages, 
    # then move onto the next day for a given range.

    article_list = []

    while date_range > 0:

        #iterate through page numbers
        for i in range(1,100): 
            response = requests.get(url+'&begin_date='+str(search_date)+'&end_date='+
                str(search_date)+'&fl=lead_paragraph'+'&page='+str(i)+'&api-key='+api_key)
            response_data = response.json()

            #check if no results found
            hit_count = response_data['response']['meta']['hits']
            if response_data['response']['meta']['hits'] == 0:
                break
            else:
                for doc in response_data['response']['docs']:
                    article_text = doc
                    if article_text != None:
                        article_list.append(article_text)

        #iterate through dates
        date_range -=1 
        search_date -=1

    # Print result to text file
    text_file = open('NYT_articles.txt','w')
    text_file.write(str(article_list))

# preprocessTopicEngine takes in the name to a text file that contains article text

def preprocessTopicEngine (topic_tfidf,text_file):

    # Print result to text file

    article_list = eval(open(text_file,'r').read())

    topic_tfidf.return_article_dict(article_list)
    # topic_tfidf.return_tfidf_dict()

    # text_file = open('NYT_tfidf_dict.txt','w')
    # text_file.write(str(topic_tfidf.tfidf_dict))

def GibbsSampling(docs):

    doc_list = docs
    topic_dict = {}
    vocab_dict = {}
    topic_num = 1000
    iter_num = 10
    doc_num = len(doc_list)
    alpha = 0.5
    beta = 0.5

    vocab = eval(open ('NYT_tfidf_dict.txt','r').read())
    vocab_num = len(vocab)

    # Needed count variables

    # Number of words in topic t
    n_wt = numpy.zeros(vocab_num, topic_num)
    n_wdt = numpy.zeros(doc_num)
    n_t = [0]*topic_num
    n_i = [0]*doc_num

    #dict that stores each word and the number of occurrences

    # for doc in doc_list:
    #     doc_list.append(TextParser.return_word_list(doc))

    # #initiate first guess for all the words

    for word in vocab:
        vocab_dict[word] = random.randint(0,topic_num-1)

    for doc in doc_list:
        for word in doc:
            topic = vocab_dict.get(word)
            return topic


    # for t in range(0,topic_num-1):
    #     topic_dict[t] = []

    # for doc in doc_list:
    #     for w in doc:
    #         t = vocab.get(w)
    #         if topic_dict.get(t) == None:
    #             topic_dict[t]=[]
    #         else:
    #             topic_dict[t] = topic_dict.get(t) + [w]

    #iterate to adjust guess

    # while iter_num > 0:
    #     for doc in doc_list:
    #         doc_length = len(doc)
    #         for w in doc:
    #             word_count_dict = {w:doc.count(w) for w in doc} #counts the number of words
    #             prob_t_d = word_count_dict.get(w)/doc_length #probability that topic is in the document

    #     iter_num -= 1



# runs collapsed Gibbs Sampling

# GibbsSampling()

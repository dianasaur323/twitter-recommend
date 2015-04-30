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

def resample(doc,word,topics,n_wt,n_wdt,n_t,n_i,doc_num):
    alpha = 0.5
    beta = 0.5
    topic = topics[doc][word]

    n_wt[topic][vocab_list.index((doc_list[doc])[word])]-=1
    n_wdt[doc][topic]-=1
    n_t[topic]-=1
    n_i[doc]-=1

    p = [0]*topic_num
    for t in range(topic_num):
        p[t]=(n_wt[t][vocab_list.index((doc_list[doc])[word])] + beta) \
        / (n_t[t] + vocab_num * beta) * (n_wdt[doc][t] + alpha) \
        / (n_i[doc] + topic_num * alpha)

    # for t in range(1,len(p)):
    #     p[t] += p[t - 1]

    for t in range(len(p)):
        if ((random.randint(0,topic_num-1) * p[t - 1])<p[t]):
            break

    n_wt[topic][vocab_list.index((doc_list[doc])[word])]+=1
    n_wdt[doc][topic]+=1
    n_t[topic]+=1
    n_i[doc]+=1

    return t


def GibbsSampling(docs):

    doc_list = docs
    topic_dict = {}
    topic_num = 5
    iter_num = 10
    doc_num = len(doc_list)


    vocab = eval(open ('NYT_tfidf_dict.txt','r').read())
    vocab_list = vocab.keys()
    vocab_num = len(vocab)


    # Needed count variables

    # Number of words w in topic t
    n_wt = numpy.zeros((topic_num,vocab_num))
    # Number of words in doc i that are in topic t
    n_wdt = numpy.zeros((doc_num,topic_num))
    n_t = [0]*topic_num
    n_i = [0]*doc_num

    #dict that stores each word and the number of occurrences

    # for doc in doc_list:
    #     doc_list.append(TextParser.return_word_list(doc))

    # Initiate first guess for all the words
    # Create an indexed collection of topics
    topics = []
    for doc in range(doc_num):
        topic_list = []
        doc_length = len(doc_list[doc])
        topics.append([0]*doc_length)
        for word in range(doc_length):
            topic = random.randint(0,topic_num-1)
            topic_list = topic_list + [topic]

            # Increment counts
            if (doc_list[doc])[word] in vocab_list:
                topics[doc][word]=topic
                n_wt[topic][vocab_list.index((doc_list[doc])[word])]+=1
                n_wdt[doc][topic]+=1
                n_t[topic]+=1
                n_i[doc]+=1

    # Iterate to improve on probabilities
    for i in range(iter_num):
        # for all words, readjust topic
        for doc in range(doc_num):
            doc_length = len(doc_list[doc])
            for word in range(doc_length):
                topic = resample(doc,word,topics,n_wt,n_wdt,n_t,n_i,doc_num)
                topics[doc][word]=topic

    print topics






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
# TopicEngine implements the latent  dirichlet allocation as described
# in Blei et al. (2003) using collapsed Gibbs Sampling described in 
# Griffiths and Steyvers (2004).

import requests
import json
import numpy
import TextParser
import random
import PreProcessor

class TopicEngine(object):

    def __init__(self,docs):

        self.doc_list = docs
        self.doc_num = len(self.doc_list)

        self.vocab = list(set(eval(open ('word_list_total.txt','r').read())))
        self.vocab_num = len(self.vocab)

        self.alpha = 0.5
        self.beta = 0.5

        self.topic_num = 100
        self.iter_num = 50 #too few, but takes too long to run

        self.theta_sum = numpy.zeros((self.doc_num, self.topic_num))
        self.phi_sum = numpy.zeros((self.topic_num, self.vocab_num))
        self.theta = self.theta_sum
        self.phi = self.phi_sum
        self.stats_num = 0

        # Needed count variables

        # Number of words w in topic t
        self.n_wt = numpy.zeros((self.topic_num,self.vocab_num))
        # Number of words in doc i that are in topic t
        self.n_wdt = numpy.zeros((self.doc_num,self.topic_num))
        self.n_t = [0]*self.topic_num
        self.n_i = [0]*self.doc_num

        self.topics = []
        

    def resample(self,doc,word):
        topic = self.topics[doc][word]

        self.n_wt[topic][self.vocab.index((self.doc_list[doc])[word])]-=1
        self.n_wdt[doc][topic]-=1
        self.n_t[topic]-=1
        self.n_i[doc]-=1

        p = [0]*self.topic_num
        for t in range(self.topic_num):
            p[t]=(self.n_wt[t][self.vocab.index((self.doc_list[doc])[word])] + self.beta) \
            / (self.n_t[t] + self.vocab_num * self.beta) * (self.n_wdt[doc][t] + self.alpha) \
            / (self.n_i[doc] + self.topic_num * self.alpha)

        # for t in range(1,len(p)):
        #     p[t] += p[t - 1]

        for t in range(len(p)):
            if ((random.randint(0,self.topic_num-1) * p[t - 1])<p[t]):
                break

        self.n_wt[topic][self.vocab.index((self.doc_list[doc])[word])]+=1
        self.n_wdt[doc][topic]+=1
        self.n_t[topic]+=1
        self.n_i[doc]+=1

        return t

    def trackProbabilities(self):
        for doc in range(self.doc_num):
            for t in range(self.topic_num):
                self.theta_sum[doc][t] += (self.n_wdt[doc][t] + self.alpha) \
                / (self.n_i[doc] + self.topic_num * self.alpha)

        for t in range(self.topic_num):
            for w in range(self.vocab_num):
                self.phi_sum[t][w] += (self.n_wt[t][self.vocab.index(self.vocab[w])] + self.beta) \
                / (self.n_t[t] + self.vocab_num * self.beta)

        self.stats_num +=1

    def get_theta(self):
        self.theta = self.theta_sum / self.stats_num
        self.phi = self.phi_sum / self.stats_num

        text_file = open('theta.txt','w')
        text_file.write(str(self.theta))

        text_file = open('phi.txt','w')
        text_file.write(str(self.phi))

    def GibbsSampling(self):

        # Initiate first guess for all the words
        # Create an indexed collection of topics

        print "starting Gibbs sampler"

        for doc in range(self.doc_num):
            doc_length = len(self.doc_list[doc])
            self.topics.append([0]*doc_length)
            print "randomly assigning doc " + str(doc) + " of " + str(self.doc_num)
            for word in range(doc_length):
                topic = random.randint(0,self.topic_num-1)

                # Increment counts
                if (self.doc_list[doc])[word] in self.vocab:
                    self.topics[doc][word]=topic
                    self.n_wt[topic][self.vocab.index((self.doc_list[doc])[word])]+=1
                    self.n_wdt[doc][topic]+=1
                    self.n_t[topic]+=1
                    self.n_i[doc]+=1

        print "finished generating first random guess"

        # Iterate to improve on probabilities
        for i in range(self.iter_num):
            # for all words, readjust topic
            for doc in range(self.doc_num):
                doc_length = len(self.doc_list[doc])
                print "readjusting LDA on doc " + str(doc) + " of " + str(self.doc_num)
                for word in range(doc_length):
                    topic = self.resample(doc,word)
                    self.topics[doc][word]=topic

            self.trackProbabilities()
            # as a status update
            print "topic engine on iteration: " + str(i)

        # print topics to document
        text_file = open('topics.txt','w')
        text_file.write(str(self.topics))
        numpy.save('n_wt',self.n_wt)
        numpy.save('n_t',self.n_t)
        numpy.save('n_wdt',self.n_wdt)

        self.get_theta()










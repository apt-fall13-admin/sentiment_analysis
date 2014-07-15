import sys
import json
from pprint import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1],'r')
    tweet_file = open(sys.argv[2],'r')
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    #afinn_file = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    #pprint(scores)
    tweets=[]
    new_word_scores = {}
    #tweet_file = open("output.txt")
    for line in tweet_file:
    	tweets.append(json.loads(line))
    for tweet in tweets:
    	if "text" in tweet:
    		#print tweet["text"]
    		sent_score = 0 
    		for word in tweet["text"].split(' '):
    			#print word
    			if word in scores:
    				sent_score = sent_score + scores[word]
    		#print sent_score
    		for word in tweet["text"].split(' '):
    			#print word
    			if word not in scores and word in new_word_scores:
    				new_word_scores[word] += sent_score		
    			elif word not in scores and word not in new_word_scores:
    				new_word_scores[word] = sent_score	
    
    for key,value in new_word_scores.items():
    	print key + " " +str(value)

if __name__ == '__main__':
    main()

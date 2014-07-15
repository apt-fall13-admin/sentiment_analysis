import sys
import json
from pprint import pprint
from collections import defaultdict

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1],'r')
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    tweets=[]
    hashtag_dict = defaultdict(int)
    #tweet_file = open("output.txt")
    count = 1;
    for line in tweet_file:
        tweets.append(json.loads(line))
    for tweet in tweets:
        if 'entities' in tweet:
            if tweet['entities']['hashtags']:
                for hashtag in tweet['entities']['hashtags']:
                    if hashtag['text'] in hashtag_dict:
                        hashtag_dict[hashtag['text']]+=1
                    else:
                        hashtag_dict[hashtag['text']]=1
        #print "Hi"
            #pprint(hashtag_array) 
        '''
                    if word in freq:
                        word=word.strip()
                        freq[word] = freq[word]+1
                        #print word+" "+str(freq[word])
                        count+=1
                    else:
                        word=word.strip()
                        freq[word]=1
                        #print word+" "+str(freq[word])
                        count+=1
                        '''

                       
    for w in sorted(hashtag_dict, key=hashtag_dict.get, reverse=True):
        to_print = w + " " + str(hashtag_dict[w])
        count +=1
        print to_print.encode('utf-8')
        if count>10:
            break


if __name__ == '__main__':
    main()
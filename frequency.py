import sys
import json

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
    freq = {}
    #tweet_file = open("output.txt")
    count = 0;
    for line in tweet_file:
        tweets.append(json.loads(line))
    for tweet in tweets:
        if "text" in tweet:
            #print tweet["text"] 
                for word in tweet["text"].split(' '):
                #print word
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
                    
    #print count                    
    for key,value in freq.items():
        t_freq = float(value)/count
        to_print = key + " " + str(t_freq)
        print to_print.encode('utf-8');

if __name__ == '__main__':
    main()
            
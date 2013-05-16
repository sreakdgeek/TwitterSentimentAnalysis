import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def computeTermScore(word):
    return 0.0

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    # Build score dictionary
    scores = {} 
    for line in sent_file:
      term, score  = line.split("\t")
      scores[term] = int(score)

    # Build the tweet_file in memory with tweet text
    tweet_data = []
    for line in tweet_file:
	response = json.loads(line)
	if "text" in response.keys():
		tweet_data.append(response["text"].encode('utf-8'))

    # Compute the tweet sentiment score
    tweet_scores = {}
    for item in tweet_data:
        term_score = 0.0
	temp = 0.0
	words = item.split()
	for word in words:
		if word in scores.keys():
			temp = float(temp) + float(scores[word])
		else:
			temp = float(temp) + 0.0
        tweet_scores[item] = float(temp)

    # Compute the term sentiment score
    for item in tweet_data:
        term_score = 0.0
	temp = 0.0
	words = item.split()
	for word in words:
		if word in scores.keys():
			term_score = float(scores[word])
		else:
			term_score = float(tweet_scores[item])
		print "%s %f" % (word, term_score)
        
if __name__ == '__main__':
    main()

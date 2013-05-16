import sys
import json

#def lines(fp):
#    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary

    # Build the tweet_file in memory with tweet text
    tweet_data = []
    for line in tweet_file:
	response = json.loads(line)
	if "text" in response.keys():
		#if "lang" in response.keys():
			#if "en" in response["lang"]:
		tweet_data.append(response["text"].encode('utf-8'))
    
	
    tweet_scores = {}
    # Computation of tweet scores
    # For each word in tweet line
    # if the scores[word] exist, then tweet_scores[word] = scores[word] else

    for item in tweet_data:
        temp = 0.0
	words = item.split()
	for word in words:
		if word in scores.keys():
			temp = float(temp) + float(scores[word])
		else:
			temp = float(temp) + 0.0
	tweet_scores[item] = float(temp)
	print '%f' % tweet_scores[item]

if __name__ == '__main__':
    main()


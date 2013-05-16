import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    # Build the tweet_file in memory with tweet text
    tweet_data = []
    for line in tweet_file:
	response = json.loads(line)
	if "text" in response.keys():
		tweet_data.append(response["text"].encode('utf-8'))

    # Compute the term and word count
    term_count = dict.fromkeys(tweet_data, 0)

    word_count = 0.0 
    for item in tweet_data:
        words = item.split()
	for word in words:
            word_count += 1.0
            if word in term_count:
               term_count[word] = term_count[word] + 1.0
            else:
               term_count[word] = 1.0
	    	    
    # Compute the term frequency
    term_frequency = {}
    for item in tweet_data:
        words = item.split()
	for word in words:
            term_frequency[word] = float(term_count[word])/float(word_count)
            print "%s %f" % (word, term_frequency[word])
        
if __name__ == '__main__':
    main()

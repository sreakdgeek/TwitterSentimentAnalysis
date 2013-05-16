import sys
import json

def main():

    tweet_file = open(sys.argv[1])
    hash_list = []
    hash_scores = {}
    hash_tag = ""
  
    # Build the tweet_file in memory with tweet text

    for line in tweet_file:
        response = json.loads(line)
        if "entities" in response.keys():
            hash_list = response["entities"]["hashtags"]
            if len(hash_list) != 0: 
               if "text" in hash_list[0]:
                    hash_tag = hash_list[0]["text"].encode("utf-8")
                    if hash_tag in hash_scores:
                        hash_scores[hash_tag] += 1
                    else:
                        hash_scores[hash_tag] = 1

    # print top 10
    counter = 0
    for hash_tag in sorted(hash_scores, key=hash_scores.get, reverse=True):
        print "%s %f" % (hash_tag, float(hash_scores[hash_tag]))
        counter = counter + 1
        if counter == 10:
            break

if __name__ == '__main__':
    main()


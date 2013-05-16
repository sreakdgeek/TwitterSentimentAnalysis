import sys
import json

def main():

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
  
    states = {
       "VERMONT": "VT", 
       "GEORGIA": "GA", 
       "IOWA": "IA", 
       "Armed Forces Pacific": "AP", 
       "GUAM": "GU", 
       "KANSAS": "KS", 
       "FLORIDA": "FL", 
       "AMERICAN SAMOA": "AS", 
       "NORTH CAROLINA": "NC", 
       "HAWAII": "HI", 
       "NEW YORK": "NY", 
       "CALIFORNIA": "CA", 
       "ALABAMA": "AL", 
       "IDAHO": "ID", 
       "FEDERATED STATES OF MICRONESIA": "FM", 
       "Armed Forces Americas": "AA", 
       "DELAWARE": "DE", 
       "ALASKA": "AK", 
       "ILLINOIS": "IL", 
       "Armed Forces Africa": "AE", 
       "SOUTH DAKOTA": "SD", 
       "CONNECTICUT": "CT", 
       "MONTANA": "MT", 
       "MASSACHUSETTS": "MA", 
       "PUERTO RICO": "PR", 
       "Armed Forces Canada": "AE", 
       "NEW HAMPSHIRE": "NH", 
       "MARYLAND": "MD", 
       "NEW MEXICO": "NM", 
       "MISSISSIPPI": "MS", 
       "TENNESSEE": "TN", 
       "PALAU": "PW", 
       "COLORADO": "CO", 
       "Armed Forces Middle East": "AE", 
       "NEW JERSEY": "NJ", 
       "UTAH": "UT", 
       "MICHIGAN": "MI", 
       "WEST VIRGINIA": "WV", 
       "WASHINGTON": "WA", 
       "MINNESOTA": "MN", 
       "OREGON": "OR", 
       "VIRGINIA": "VA", 
       "VIRGIN ISLANDS": "VI", 
       "MARSHALL ISLANDS": "MH", 
       "WYOMING": "WY", 
       "OHIO": "OH", 
       "SOUTH CAROLINA": "SC", 
       "INDIANA": "IN", 
       "NEVADA": "NV", 
       "LOUISIANA": "LA", 
       "NORTHERN MARIANA ISLANDS": "MP", 
       "NEBRASKA": "NE", 
       "ARIZONA": "AZ", 
       "WISCONSIN": "WI", 
       "NORTH DAKOTA": "ND", 
       "Armed Forces Europe": "AE", 
       "PENNSYLVANIA": "PA", 
       "OKLAHOMA": "OK", 
       "KENTUCKY": "KY", 
       "RHODE ISLAND": "RI", 
       "DISTRICT OF COLUMBIA": "DC", 
       "ARKANSAS": "AR", 
       "MISSOURI": "MO", 
       "TEXAS": "TX", 
       "MAINE": "ME"
    }

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # Build the tweet_file in memory with tweet text
    addr_list = []
    tweet_scores = {}
    temp_state_code = ""

    for line in tweet_file:
        response = json.loads(line)
        if "text" in response.keys():
            if "user" in response.keys():
                addr_list = response["user"]["location"].encode('utf-8').split(',')
                if len(addr_list) >= 2:
                    if "USA" in addr_list[len(addr_list)-1]:
                        state_code = addr_list[len(addr_list)-2].strip()

                        if len(state_code) != 2:
                           if state_code.upper() in states:
                              temp_state_code = states[state_code.upper()] 
                           else:
                               temp_state_code = "NA"
                           state_code = temp_state_code

                        if len(state_code) == 2:
                            words = response["text"].encode('utf-8').split()
                            temp = 0.0
                            for word in words:
                                if word in scores.keys():
                                     temp = float(temp) + float(scores[word])
                                else:
                                     temp = float(temp) + 0.0
                                if state_code in tweet_scores: 
                                    tweet_scores[state_code] = tweet_scores[state_code] + float(temp)
                                else:
                                    tweet_scores[state_code] = float(temp)

    if len(tweet_scores) != 0:
        print max(tweet_scores, key=tweet_scores.get)

    #inverse = [(value, key) for key, value in tweet_scores.items()]
    # if len(inverse) != 0:
    #      print max(inverse)[1]

    #stats = {'a':1000, 'b':3000, 'c': 100}
    #inverse = [(value, key) for key, value in stats.items()]
    #print max(inverse)[1]

if __name__ == '__main__':
    main()


# filter_formal_name.py
# Author: Kevin Wittmer
#
# Filters a raw dataset of JSON formatted tweets by formal company name. Formal
# company names for the top 100 brands are listed in formal_company_names.txt.
# A tweet passes through this filter if the tweet string contains one of the
# desired company names. Accepts as input one .json file containing tweets in
# JSON objects and outputs a .json file containing those tweets that meet the
# filtering criteria.

import json
import string
import sys

from collections import OrderedDict


"""
Returns true if a JSON-formatted tweet contains a formal company name and false
otherwise. Invalid punctuation is first removed from the tweet text, then the
text is split into individual words. Company names without spaces are checked
to determine if they appear in this list of words. Then company names with 
spaces are checked to determine if they appear as a substring of the entire 
tweet text string.
"""
def contains_formal_company_name(tweet):
    # Add a new empty list to the tweet JSON object to store company names in
    # the tweet
    tweet["companies"] = []

    # Extract the tweet text from the json object and remove all punctuation
    # not in company names
    tweet_text = str(tweet["text"].encode("ascii", "ignore"))
    tweet_text = tweet_text.translate(string.maketrans("",""),
                                      invalid_punctuation)

    # Split the tweet into individual words stored in a list, then determine
    # what company names with no spaces are in this list
    words_in_tweet = tweet_text.split()
    for name in company_names["no_spaces"]:
        if name in words_in_tweet:
            tweet["companies"].append(name)

    # Now search for company names with spaces in the entire tweet string (with
    # punctuation removed)
    for name in company_names["with_spaces"]:
        if name in tweet_text:
            tweet["companies"].append(name)

    # Returns true if a company was found in the tweet
    return len(tweet["companies"]) > 0


"""
Returns true if the tweet meets the filtering criteria and false otherwise. The
current filtering criteria are that the tweet is in English and it contains a 
formal company name. This function is here to make it easier to modify the
script later if the filtering criteria needs to be changed.
"""
def meets_criteria(tweet):
    return tweet["tweetOwner"]["language"] == "en" and \
           contains_formal_company_name(tweet)


"""
Reads in raw tweets from input .json file, performs filtering, and writes 
filtered tweets to output .json file.
"""
def main():
    # Open output .json data file provided at command line
    output_file = open(sys.argv[2], "w")

    # Write tweets in input file that pass filtering criteria to output file
    with open(sys.argv[1], "r") as input_file:
        for line in input_file:
            tweet = json.loads(line, object_pairs_hook=OrderedDict)
            if meets_criteria(tweet):
                json.dump(tweet, output_file)
                output_file.write("\n")

    # Close the opened output file
    output_file.close()


"""
Performs preprocessing and calls the main filtering function. Initializes 
company_names as a global dictionary that stores two lists: company names with
spaces and names without spaces. Also sets a global string containing 
punctuation characters to be ignored during filtering.
"""
if __name__ == "__main__":
    # Check for proper command line arguments
    if len(sys.argv) != 3:
        print "Usage: filter_formal_name.py <input_file.json> <output_file.json>"
        sys.exit()
    
    # Load 100 company names into a dictionary separated into two lists: one
    # list containing names with spaces, the other without spaces
    company_names = { "no_spaces": [], "with_spaces": [] }
    with open("formal_company_names.txt", "r") as companies_file:
        for line in companies_file:
            name = line.strip()
            if ' ' in name:
                company_names["with_spaces"].append(name)
            else:
                company_names["no_spaces"].append(name)

    # String of punctuation to remove from tweet text
    invalid_punctuation = "!\"#$%()*+,./:;<=>?@[\\]^_`{|}~"

    # Begin filtering execution
    main()

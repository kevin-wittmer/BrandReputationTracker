import json
import string
import sys

from collections import OrderedDict

# Returns true if the company name appears in the tweet, false otherwise
def contains_company_name(tweet):
    # Add a new empty list to the tweet json object to store company names in
    # the tweet
    tweet["companies"] = []

    # Extract the tweet text from the json object and remove all punctuation
    # not in company names
    tweet_text = str(tweet["text"].encode("ascii", "ignore"))
    tweet_text = tweet_text.translate(string.maketrans("",""), invalid_punctuation)

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


# Returns true if the tweet is in English, false otherwise
def is_english(tweet):
    return tweet["tweetOwner"]["language"] == "en"


# Returns true if the tweet meets the filtering criteria, false otherwise
def meets_criteria(tweet):
    return is_english(tweet) and contains_company_name(tweet)


def main():
    # Open output .json data file provided at command line
    output_file = open(sys.argv[2], "w")

    # Write tweets in input .json file that pass filtering criteria to
    # output .json data file
    with open(sys.argv[1], "r") as input_file:
        for line in input_file:
            tweet = json.loads(line, object_pairs_hook=OrderedDict)
            if meets_criteria(tweet):
                json.dump(tweet, output_file)
                output_file.write("\n")

    # Close the opened output file
    output_file.close()

    
if __name__ == "__main__":
    # Check for proper command line arguments
    if len(sys.argv) != 3:
        print "Usage: filter.py <input_file.json> <output_file.json>"
        sys.exit()
    
    # Load 100 company names into a dictionary separated into two lists: one
    # list containing names with spaces, the other without spaces
    company_names = { "no_spaces": [], "with_spaces": [] }
    with open("company_names.txt", "r") as companies_file:
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

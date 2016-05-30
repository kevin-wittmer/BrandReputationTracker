import json
import sys

from collections import OrderedDict

# Returns true if the company name appears in the tweet, false otherwise
def contains_company_name(tweet, company_names):
    for name in company_names:
        if name in tweet["text"].lower():
            return True

    return False


# Returns true if the tweet is in English, false otherwise
def is_english(tweet):
    return tweet["tweetOwner"]["language"] == "en"


# Returns true if the tweet meets the filtering criteria, false otherwise
def meets_criteria(tweet, company_names):
    return is_english(tweet) and contains_company_name(tweet, company_names)


def main():
    # Check for proper command line arguments
    if len(sys.argv) != 3:
        print "Usage: filter.py <input_file.json> <output_file.json>"
        return

    # Store company names in a list and remove trailing \n characters
    company_names = open("company_names.txt", "r").readlines()
    company_names = [name.strip().lower() for name in company_names]

    # Open output data file
    output_filename = "../filtered_data/" + sys.argv[2]
    output_file = open(output_filename, "w")

    # Open input data file and read lines
    input_filename = "../raw_data/" + sys.argv[1]
    input_file = open(input_filename, "r")
    lines = input_file.readlines()

    # Write each tweet to output file if it meets the filtering criteria
    for line in lines:
        tweet = json.loads(line, object_pairs_hook=OrderedDict)
        if meets_criteria(tweet, company_names):
            json.dump(tweet, output_file)
            output_file.write("\n")

    # Close all opened files
    input_file.close()
    output_file.close()

    
if __name__ == "__main__":
    main()

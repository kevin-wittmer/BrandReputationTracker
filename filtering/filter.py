import json

from collections import OrderedDict

def contains_company_name(tweet, company_names):
    for name in company_names:
        if name in tweet["text"].lower():
            print name
            return True

    return False


def is_english(tweet):
    return tweet["tweetOwner"]["language"] == "en"


def meets_criteria(tweet, company_names):
    return is_english(tweet) and contains_company_name(tweet, company_names)


def main():
    # Store company names in a list and remove trailing \n characters
    company_names = open("company_names.txt", "r").readlines()
    company_names = [name.strip().lower() for name in company_names]

    # Open output data file
    output_file = open("sample_output.json", "w")

    # Open sample data file and read lines
    input_file = open("sample_data.json", "r")
    lines = input_file.readlines()

    # Write each tweet to output_file if it meets the filtering criteria
    for line in lines:
        tweet = json.loads(line, object_pairs_hook=OrderedDict)
        if meets_criteria(tweet, company_names):
            json.dump(tweet, output_file)
            output_file.write("\n")

    # Close all opened files
    output_file.close()
    input_file.close()

    
if __name__ == "__main__":
    main()

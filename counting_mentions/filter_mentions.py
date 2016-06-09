# filter_mentions.py
# Author: Kevin Wittmer
# TODO description

import json
import sys

from collections import OrderedDict

def contains_handle(tweet, handles):
    for mention in tweet["parsedMentions"]:
        if mention["userScreenName"].lower() in handles:
            return True

    return False


def main():
    # Read list of handles and remove @ symbol and newline character
    with open("twitter_handles.txt", "r") as handles_file:
        handles = handles_file.readlines()
        handles = [name.strip('@\n').lower() for name in handles]

    output_filename = sys.argv[2]
    output_file = open(output_filename, "w")

    input_filename = "../raw_data/" + sys.argv[1]
    input_file = open(input_filename, "r")
    lines = input_file.readlines()

    for line in lines:
        tweet = json.loads(line, object_pairs_hook=OrderedDict)
        if contains_handle(tweet, handles):
            json.dump(tweet, output_file)
            output_file.write("\n")

    input_file.close()
    output_file.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: filter_mentions.py <input_file.json> <output_file.json>"
    else:
        main()

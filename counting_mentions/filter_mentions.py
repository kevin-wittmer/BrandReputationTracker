# count_mentions.py
# Author: Kevin Wittmer
# TODO description

import json

from collections import OrderedDict

def contains_handle(tweet, handles):
    for mention in tweet["parsedMentions"]:
        if mention["userScreenName"].lower() in handles:
            print mention["userScreenName"]
            return True

    return False


def main():
    with open("twitter_handles.txt", "r") as handles_file:
        handles = handles_file.readlines()
        handles = [name.strip('@\n').lower() for name in handles]

    output_filename = "test.json"
    output_file = open(output_filename, "w")

    input_filename = "../raw_data/collection_brands.0.json"
    input_file = open(input_filename, "r")
    lines = input_file.readlines()

    for line in lines:
        tweet = json.loads(line, object_pairs_hook=OrderedDict)
        if contains_handle(tweet, handles):
            print tweet
            json.dump(tweet, output_file)
            output_file.write("\n")

    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()

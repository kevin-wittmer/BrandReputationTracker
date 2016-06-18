import csv
import json
import re
import string
import sys

# Cleans the tweet text by removing special characters, RT, punctuation, and extra whitespace
def clean(tweet_text):
    tweet_text = tweet_text.encode("ascii", "ignore").replace("\n", " ")
    tweet_text = re.sub(r"(?:\@|https?\://)\S+", "", tweet_text)
    tweet_text = tweet_text.replace("http", "").replace("RT", "")
    tweet_text = tweet_text.translate(string.maketrans("",""), string.punctuation)
    tweet_text = " ".join(tweet_text.split())
    return tweet_text


def main():
    # Open input data .json file
    input_file = open(sys.argv[1], "r")

    # Open csv file to write data to
    with open(sys.argv[2], "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["tweetId", "text"])    # header

        # For each tweet, write its ID and text to csv file
        for line in input_file:
            tweet = json.loads(line)
            tweetId = tweet["tweetId"]
            text = clean(tweet["text"])
            if text != "":
                writer.writerow([tweetId, text])

    # Print location of cleaned data
    print "Data written to:", output_file.name

    # Close the input file
    input_file.close()


if __name__ == "__main__":
    # Check for proper command line arguments
    if len(sys.argv) != 3:
        print "Usage: clean.py <input_file.json> <output_file.csv>"
    else:
        main()

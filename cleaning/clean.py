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
	# Check for proper command line arguments
	if len(sys.argv) != 3:
		print "Usage: clean.py <input_file.json> <output_file.csv>"
		return

	# Open the data and read each line as a string into a list
	input_filename = "../filtered_data/" + sys.argv[1]
	with open(input_filename, "r") as input_file:
		lines = input_file.readlines()

	# Parse the name of the csv file
	output_filename = "../cleaned_data/" + sys.argv[2]

	# Open csv file to write data to
	with open(output_filename, "w") as output_file:
		writer = csv.writer(output_file)
		writer.writerow(["tweetId", "text"])    # header

		# For each tweet, write its ID and text to csv file
		for line in lines:
			tweet = json.loads(line)
			tweetId = tweet["tweetId"]
			text = clean(tweet["text"])
			if text != "":
				writer.writerow([tweetId, text])

	# Print location of cleaned data
	print "Data written to:", output_file.name


if __name__ == "__main__":
	main()

import csv

# Split each tweet into a list of words
def stemmify(tweet_string):
	word_list = tweet_string.split()
	return word_list

# Open csv file containing tweets
csvfile = open('clean_data/collection3.csv')
csvreader = csv.DictReader(csvfile)

# Split each tweet into a list of words and print the list
for tweet in csvreader:
	stemmed_words = stemmify(tweet['text'])
	print stemmed_words

# Close the csv file
csvfile.close()

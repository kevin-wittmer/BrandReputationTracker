import csv
from nltk import stem

# Create a global stemmer object
# stemmer = stem.snowball.EnglishStemmer()
stemmer = stem.PorterStemmer()

# Splits each tweet into a list of stemmed words
def stemmify(tweet_string):
	word_list = tweet_string.split()
	stemmed_list = []
	for tag in word_list:
		stemmed_list.append(stemmer.stem(tag))
	return stemmed_list

# Open csv file containing tweets
csvfile = open('clean_data/collection3.csv')
csvreader = csv.DictReader(csvfile)

# Split each tweet into a list of words and print the list
for tweet in csvreader:
	stemmed_words = stemmify(tweet['text'])
	print stemmed_words

# Close the csv file
csvfile.close()

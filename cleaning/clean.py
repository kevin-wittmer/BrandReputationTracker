import csv
import json
import re
import string
import sys

# Cleans the tweet text by removing special characters, RT, punctuation, and extra whitespace
def clean(tweet_text):
	tweet_text = tweet_text.encode('ascii', 'ignore').replace('\n', ' ')
	tweet_text = re.sub(r"(?:\@|https?\://)\S+", "", tweet_text)
	tweet_text = tweet_text.replace('http', '').replace('RT', '')
	tweet_text = tweet_text.translate(string.maketrans("",""), string.punctuation)
	tweet_text = ' '.join(tweet_text.split())
	return tweet_text

# Check for proper command line arguments
if len(sys.argv) != 2:
    print 'Usage: clean.py <filename.json>'
    sys.exit(2)

# Open the data and read each JSON object into a list
data_file = open(sys.argv[1], 'r')
tweets = data_file.readlines()
data_file.close()

# Parse the name of the csv file
csv_filename = 'collection' + sys.argv[1].split('.')[2] + '.csv'
csv_path = '.\clean_data\\' + csv_filename

# Open csv file to write data to
with open(csv_path, 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['tweetId', 'text'])    # header

    # For each English tweet, write its ID and text to csv file
    for line in tweets:
        values = json.loads(line)
        if values['tweetOwner']['language'] == 'en':
            tweetId = values['tweetId']
            text = clean(values['text'])
            if text != '':
            	writer.writerow([tweetId, text])

# Print location of cleaned data and close csv file
print 'Data written to:', csvfile.name
csvfile.close()

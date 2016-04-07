import json

# Open the data and read each JSON object into a list
data_file = open('collection_brands.11.json', 'r')
tweets = data_file.readlines()
data_file.close()

# Load each JSON object and add English tweets to new list
english_tweets = []
for line in tweets:
    values = json.loads(line)
    if values['tweetOwner']['language'] == 'en':
        english_tweets.append(values)

# Print the number of English tweets retrieved
print len(english_tweets)

import json

# Open the data and read each JSON object into a list
data_file = open('sample_data.json', 'r')
tweets = data_file.readlines()

# Load each JSON object and print the tweetId
for line in tweets:
    values = json.loads(line)
    print values["tweetId"]

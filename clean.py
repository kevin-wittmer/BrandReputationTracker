import csv
import json

# Open the data and read each JSON object into a list
data_file = open('sample_data.json', 'r')
tweets = data_file.readlines()
data_file.close()

# Open csv file to write data to
with open('clean.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['tweetId', 'text'])    # header

    # Write each ID and tweet to csv file
    for line in tweets:
        values = json.loads(line)
        #if values['tweetOwner']['language'] == 'en':
        writer.writerow([values['tweetId'],
            values['text'].encode('ascii', 'ignore')])

csvfile.close()

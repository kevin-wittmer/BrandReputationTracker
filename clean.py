import csv
import json
import sys

# Check for proper command line arguments
if len(sys.argv) != 2:
    print 'Usage: clean.py <filename.json>'
    sys.exit(2)

# Open the data and read each JSON object into a list
data_file = open(sys.argv[1], 'r')
tweets = data_file.readlines()
data_file.close()

# Parse the name of the csv file
csv_filename = sys.argv[1]
csv_filename = csv_filename[0:10] + csv_filename[18:20] + '.csv'

# Open csv file to write data to
with open(csv_filename, 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['tweetId', 'text'])    # header

    # For each English tweets, write each ID and text to csv file
    for line in tweets:
        values = json.loads(line)
        if values['tweetOwner']['language'] == 'en':
            writer.writerow([values['tweetId'],
                values['text'].encode('ascii', 'ignore')])

# Print location of cleaned data and close csv file
print 'Data written to:', csvfile.name
csvfile.close()

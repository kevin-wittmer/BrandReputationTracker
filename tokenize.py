import csv

# Open csv file containing tweets
with open('collection3.csv') as csvfile:
	reader = csv.DictReader(csvfile)

	# Print out each tweet without leading RT
	for row in reader:
		print row['text'].strip('RT ')

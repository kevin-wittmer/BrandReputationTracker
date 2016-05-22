import json

# Store filtering keywords in a list and remove trailing \n characters
filtering_criteria = open('filtering_criteria.txt', 'r').readlines()
filtering_criteria = [keyword.strip().lower() for keyword in filtering_criteria]

json_file = open('C:\Users\Kevin\Documents\BrandReputationTracker\\raw_data\collection_brands.11.json', 'r')
tweet_strings = json_file.readlines()
for line in tweet_strings:
	values = json.loads(line)
	for keyword in filtering_criteria:
		if keyword in values['text'].lower():
			print values['text'].encode('ascii', 'ignore')
			print keyword

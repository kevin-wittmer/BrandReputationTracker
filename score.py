import csv
from nltk import stem

# Create a global stemmer object
stemmer = stem.snowball.EnglishStemmer()
# stemmer = stem.PorterStemmer()

# Splits each tweet into a list of stemmed words
def stemmify(tweet_string):
	word_list = tweet_string.split()
	stemmed_list = []
	for tag in word_list:
		stemmed_list.append(stemmer.stem(tag))
	return stemmed_list

# Creates a map from the csv file's keyword to their scores
def create_map(filename):
	filereader = csv.DictReader(open(filename))
	dictionary = {}
	for line in filereader:
		dictionary[line['keyword']] = float(line['score'])
	return dictionary

def score(set_of_words, score_map):
	score = 0
	for stemword in set_of_words:
		if stemword in score_map:
			score = score + score_map[stemword]
	return score

# Open csv file containing tweets
csvfile = open('clean_data/collection3.csv')
csvreader = csv.DictReader(csvfile)

# Open output csv file and write header row
output_file = open('output.csv', 'wb')
output_writer = csv.writer(output_file)
output_writer.writerow(['tweetId', 'CommunityNegative', 'CommunityPositive', 'CoolNegative', 'CoolPositive',
	'ExcitingNegative', 'ExcitingPositive', 'FriendlyNegative', 'FriendlyPositive', 'GoodsQualityNegative',
	'GoodsQualityPositive', 'InnovativeNegative', 'InnovativePositive', 'InternetMobileNegative',
	'InternetMobilePositive', 'PersonalRelationshipsNegative', 'PersonalRelationshipsPositive',
	'PriceNegative', 'PricePositive', 'ServiceQualityNegative', 'ServiceQualityPositive', 'SocialResponsibilityNegative',
	'SocialResponsibilityPositive', 'SustainabilityNegative', 'SustainabilityPositive', 'TrustworthyNegative',
	'TrustworthyPositive'])

# For each indicator, generate a map from each keyword to its score
community_negative_map = create_map('keywords/community_negative.csv')
community_positive_map = create_map('keywords/community_positive.csv')
cool_negative_map = create_map('keywords/cool_negative.csv')
cool_positive_map = create_map('keywords/cool_positive.csv')
exciting_negative_map = create_map('keywords/exciting_negative.csv')
exciting_positive_map = create_map('keywords/exciting_positive.csv')
friendly_negative_map = create_map('keywords/friendly_negative.csv')
friendly_positive_map = create_map('keywords/friendly_positive.csv')
goodsquality_negative_map = create_map('keywords/goodsquality_negative.csv')
goodsquality_positive_map = create_map('keywords/goodsquality_positive.csv')
innovative_negative_map = create_map('keywords/innovative_negative.csv')
innovative_positive_map = create_map('keywords/innovative_positive.csv')
internetmobile_negative_map = create_map('keywords/internetmobile_negative.csv')
internetmobile_positive_map = create_map('keywords/internetmobile_positive.csv')
personalrelationships_negative_map = create_map('keywords/personalrelationships_negative.csv')
personalrelationships_positive_map = create_map('keywords/personalrelationships_positive.csv')
price_negative_map = create_map('keywords/price_negative.csv')
price_positive_map = create_map('keywords/price_positive.csv')
servicequality_negative_map = create_map('keywords/servicequality_negative.csv')
servicequality_positive_map = create_map('keywords/servicequality_positive.csv')
socialresponsibility_negative_map = create_map('keywords/socialresponsibility_negative.csv')
socialresponsibility_positive_map = create_map('keywords/socialresponsibility_positive.csv')
sustainability_negative_map = create_map('keywords/sustainability_negative.csv')
sustainability_positive_map = create_map('keywords/sustainability_positive.csv')
trustworthy_negative_map = create_map('keywords/trustworthy_negative.csv')
trustworthy_positive_map = create_map('keywords/trustworthy_positive.csv')

# Split each tweet into a list of words and print the list
for tweet in csvreader:
	stemmed_words = set(stemmify(tweet['text']))
	output_writer.writerow([tweet['tweetId'], score(stemmed_words, community_negative_map), score(stemmed_words, community_positive_map),
		score(stemmed_words, cool_negative_map), score(stemmed_words, cool_positive_map), score(stemmed_words, exciting_negative_map),
		score(stemmed_words, exciting_positive_map), score(stemmed_words, friendly_negative_map), score(stemmed_words, friendly_positive_map),
		score(stemmed_words, goodsquality_negative_map), score(stemmed_words, goodsquality_positive_map), score(stemmed_words, innovative_negative_map),
		score(stemmed_words, innovative_positive_map), score(stemmed_words, internetmobile_negative_map), score(stemmed_words, internetmobile_positive_map),
		score(stemmed_words, personalrelationships_negative_map), score(stemmed_words, personalrelationships_positive_map),
		score(stemmed_words, price_negative_map), score(stemmed_words, price_positive_map), score(stemmed_words, servicequality_negative_map),
		score(stemmed_words, servicequality_positive_map), score(stemmed_words, socialresponsibility_negative_map),
		score(stemmed_words, socialresponsibility_positive_map), score(stemmed_words, sustainability_negative_map),
		score(stemmed_words, sustainability_positive_map), score(stemmed_words, trustworthy_negative_map),
		score(stemmed_words, trustworthy_positive_map)])

# Close both csv files
csvfile.close()
output_file.close()

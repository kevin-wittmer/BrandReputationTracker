import csv


def main():
	csvfile = open("tweet_counts.csv", "wb")
	writer = csv.writer(csvfile)
	writer.writerow(["Collection", "Raw", "FilteredCompanies", "FilteredMentions", "FilteredCompanies/Raw", "FilteredMentions/Raw"])

	for i in range(0, 31):
		collection = i
		raw = filtered_companies = filtered_mentions = 0
		with open("../raw_data/collection_brands." + str(i) + ".json", "r") as file:
			raw = len(file.readlines())
		with open("../filtered_data/filtered_tweets." + str(i) + ".json", "r") as file:
			filtered_companies = len(file.readlines())
		with open("filtered_by_mentions." + str(i) + ".json", "r") as file:
			filtered_mentions = len(file.readlines())
		writer.writerow([collection, raw, filtered_companies, filtered_mentions, float(filtered_companies) / raw, float(filtered_mentions) / raw])


if __name__ == "__main__":
	main()
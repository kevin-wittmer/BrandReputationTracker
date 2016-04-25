import score
import operator
output_file = open('community_negative_map.csv', 'wb')
output_writer = csv.writer(output_file)

sort_map = sorted(community_negative_map.items(), key=operator.itemgetter(1))
print sort_map.reverse()
output_writer.writerows(sort_map)

#sort_map = sorted(community_negative_map.items(), key=operator.itemgetter(1))
#print sort_map.reverse()



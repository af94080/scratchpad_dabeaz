from collections import Counter
tot_by_route = Counter()

for record in records:
	tot_by_route[record.route] += int(record.rides)

tot_by_route['22']

tot_by_route.most_common(3)
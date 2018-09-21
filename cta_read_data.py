def read_data(filename):
	from collections import namedtuple
	Row = namedtuple(Row, ['route', 'date', 'daytype', 'rides'])
	import csv

	records = []

	with open(filename) as f:
		rows = csv.reader(f)
		header = next(rows)

		for row in rows:
			route = row[0]
			date = row[1]
			daytype = row[2]
			rides = int(row[3])

			records.append(Row(route, date, daytype, rides))

	return records
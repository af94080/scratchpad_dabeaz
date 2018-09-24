
def read_data(file):
	
	import csv
	from collections import namedtuple

	records = []

	with open(file) as f:
		rows = csv.reader(f)
		header = next(rows)
		Row = namedtuple('Row', header)

		for row in rows:
			records.append(Row._make(row))

	return records		
			


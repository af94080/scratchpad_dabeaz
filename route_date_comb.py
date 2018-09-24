route_date = {}

for record in records:
	route_date[record.route, record.date] = record.rides

route_date['22', '04/09/2007']	
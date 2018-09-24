>>> file = '/Users/arulfrancis/Data/ctabus.csv'
>>> f = open(file)
>>> import csv
>>> rows = csv.reader(f)
>>> next(rows)
['route', 'date', 'daytype', 'rides']
>>> rt22 = (row for row in rows if row[0] == '22')
>>> next(rt22)
['22', '01/01/2001', 'U', '7877']
>>> rides_date = ((int(row[3]), row[1]) for row in rt22)
>>> next(rides_date)
(19558, '01/02/2001')
>>> max(rides_date)
(26896, '06/11/2008')
>>> f.close()

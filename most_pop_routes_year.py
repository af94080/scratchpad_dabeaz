
# cluster the data by year 

# build a counter for each year 

file = '/Users/arulfrancis/Data/ctabus.csv'

from read_data import read_data
from collections import Counter
from collections import defaultdict

total_by_year = defaultdict(Counter)

records = read_data(file)

for record in records:
	year = record.date[-4:]
	total_by_year[year][record.route] += int(record.rides)

print(total_by_year['2016'].most_common(3))	


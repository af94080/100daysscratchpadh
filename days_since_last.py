
from datetime import date

'''
My last movie visit was a 		116 days 		ago on the 3th of Mar.
My last library visit was a 		114 days 		ago on the 5th of Mar.
My last family visit was a 		90 days 		ago on the 29th of Mar.
My last peets visit was a 		113 days 		ago on the 6th of Mar.
My last eds diner visit was a 		120 days 		ago on the 28th of Feb.

'''

visits = {
	'movie' : date(2020, 3, 3),
	'library' : date(2020, 3, 5),
	'family' : date(2020, 3, 29),
	'peets' : date(2020, 3, 6),
	'eds diner' : date(2020, 2, 28)
}

def days_since_visit(visit):
	return (date.today() - visit).days

for visit, day_of in visits.items():
	print(f'My last {visit} visit was a \
		{days_since_visit(day_of)} days \
		ago on the {day_of.strftime("%-dth of %b")}.')

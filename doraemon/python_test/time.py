import datetime
import dateutil.parser
import time

DATE = '2019-01-07T08:00:00.000000'
date_time = dateutil.parser.parse(DATE)

for s in range(5):
    date_time += datetime.timedelta(seconds=0.5)

print(date_time)

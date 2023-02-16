#!/usr/bin/python

# import time
# import datetime

# today = datetime.datetime.now()
# print ("today date =>" , today)

# other_day = datetime.datetime(2017, 4, 21, 11, 0, 0, 0)
# print ("other date =>" , other_day)
# print ("other type =>" , type(other_day))

# result = today - other_day
# ms = int(result.total_seconds() * 1000000)
# dt = datetime.timedelta(microseconds = ms)
# new_day = dt + other_day

# print ("new_day :",new_day)

# from datetime import datetime
# import calendar
# import time
# import os

# d = datetime.now()
# ts = time.mktime(d.timetuple())
# print (' utc  time=',datetime.utcfromtimestamp(ts).replace(microsecond=d.microsecond))

# d = datetime.utcnow()
# ts = calendar.timegm(d.timetuple())
# print ('local time=',datetime.fromtimestamp(ts).replace(microsecond=d.microsecond))



# import datetime
# import pytz

# now = datetime.datetime.now(tz=pytz.timezone('Asia/Taipei'))
# now_1 = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))

# nw = now - now_1

# print("taipei_now : ",now)
# print("us_eastern_now : ",now_1)
# print("nw : ",nw)
# print()

# utc_dt = datetime.datetime(2002, 10, 27, 6, 0, 0, tzinfo=pytz.utc)

# loc_dt = utc_dt.astimezone(pytz.timezone('Asia/Taipei'))
# loc_d = utc_dt.astimezone(pytz.timezone('US/Eastern'))
# fmt = '%Y-%m-%d %H:%M:%S %Z%z'
# at = loc_dt.strftime(fmt)

# ct = loc_dt - loc_d

# print("utc_data : ",utc_dt)
# print()
# print("loc_dt : ",loc_dt)
# print("loc_d : ",loc_d)
# print("date ct: ",ct)


egg = [(1, 545985180000, 'device_id_hao', 'vol', None, 12.0),
    (1, 545985180000, 'device_id_hao', 'temp', None, 38.0),
    (2, 545985300000, 'device_id_hao', 'vol', None, 220.0),
    (2, 545985300000, 'device_id_hao', 'temp', None, 39.0)
]

merged = dict()
for i in (egg):
    key = i[0:3]
    value = i[3:]
    nvalue = list(n for n in value if n is not None)
    if merged.get(key):  # if merged has this key, extend the list
        merged[key].extend(nvalue)
    else:
        merged[key] = nvalue

for v in sorted(merged.items()):
    print("value:", v)
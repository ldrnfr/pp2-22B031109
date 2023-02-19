#1 
from datetime import date, timedelta
date_new = date.today() - timedelta(5)
print(date_new)

#2
from datetime import date, timedelta
date_yesterday = date.today() - timedelta(1)
date_tomorrow = date.today() + timedelta(1)
print(date_yesterday, date.today(), date_tomorrow)

#3
from datetime import datetime
day1 = datetime.today().replace(microsecond = 0)
print(day1)

#4
from datetime import datetime
def dif_in_seconds(d1, d2):
    timedelta= d2-d1
    return timedelta.days*24*3600 

day1 = datetime.strptime('2003.08.08 07:00:00', '%Y.%m.%d %H:%M:%S')
day2 = datetime.now()
print(dif_in_seconds(day1, day2))

#Ex 1
from datetime import datetime, timedelta
dt = datetime.now() - timedelta(days=5)
print('Current Date :',datetime.now())
print('5 days before Current Date :',dt)

#Ex 2
from datetime import date
from datetime import timedelta

# Today's date
today = date.today()
print("Today is: ", today)
 
# Yesterday date
yesterday = today - timedelta(days = 1)
print("Yesterday was: ", yesterday)

tomorrow = today +timedelta(days=1)
print("Tomorrow: ",tomorrow)

#Ex 3
import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#Ex 4
from datetime import datetime

def date_diff_in_seconds(dt2, dt1):
    delta = dt2 - dt1
    return int(delta.total_seconds())

# specified
date1 = datetime.strptime('2017-09-01 00:00:00', '%Y-%m-%d %H:%M:%S')
# Current
date2 = datetime.now()

# Output
print("{} seconds".format(date_diff_in_seconds(date2, date1)))
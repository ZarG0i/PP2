#datetime Module
import datetime

x = datetime.datetime.now()
print(x)
#-------------------------------------
from datetime import date

today = date.today()
print(today)

#-------------------------------------
from datetime import datetime

current_time = datetime.now().time()
print(current_time)
#-------------------------------------
from datetime import datetime

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
#-------------------------------------
from datetime import datetime

now = datetime.now()
print(now.hour)
print(now.minute)
print(now.second)
#Creating Date Objects
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)
#-------------------------------------
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
#-------------------------------------
from datetime import datetime

dt = datetime(2026, 3, 1, 14, 30, 0)
print(dt)
#-------------------------------------
from datetime import time

t = time(10, 45, 30)
print(t)
#-------------------------------------
from datetime import datetime, date, time

d = date(2026, 3, 1)
t = time(12, 0)
combined = datetime.combine(d, t)

print(combined)
#Date formatting 
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d"))
#-------------------------------------
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
#-------------------------------------
from datetime import datetime

now = datetime.now()
print(now.strftime("%d/%m/%Y"))
#-------------------------------------
from datetime import datetime

now = datetime.now()
print(now.strftime("%B"))
#-------------------------------------
from datetime import datetime

now = datetime.now()
print(now.strftime("%A"))
#Calculating Time Differences
from datetime import date

d1 = date(2026, 3, 10)
d2 = date(2026, 3, 1)

print((d1 - d2).days)
#-------------------------------------
from datetime import datetime

dt1 = datetime(2026, 3, 1, 15, 0)
dt2 = datetime(2026, 3, 1, 12, 0)

difference = dt1 - dt2
print(difference)
#-------------------------------------
from datetime import datetime

dt1 = datetime(2026, 3, 2)
dt2 = datetime(2026, 3, 1)

difference = dt1 - dt2
print(difference.total_seconds())
#-------------------------------------
from datetime import datetime, timedelta

now = datetime.now()
future = now + timedelta(days=7)

print(future)
#-------------------------------------
from datetime import datetime, timedelta

now = datetime.now()
past = now - timedelta(hours=5)

print(past)
#Working with Timezones
from datetime import datetime
from zoneinfo import ZoneInfo

utc_time = datetime.now(ZoneInfo("UTC"))
print(utc_time)
#-------------------------------------
from datetime import datetime
from zoneinfo import ZoneInfo

almaty_time = datetime.now(ZoneInfo("Asia/Almaty"))
print(almaty_time)
#-------------------------------------
from datetime import datetime
from zoneinfo import ZoneInfo

utc_time = datetime.now(ZoneInfo("UTC"))
almaty_time = utc_time.astimezone(ZoneInfo("Asia/Almaty"))

print(almaty_time)
#-------------------------------------
from datetime import datetime
from zoneinfo import ZoneInfo

ny_time = datetime.now(ZoneInfo("America/New_York"))
print(ny_time)
#-------------------------------------
from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime.now(ZoneInfo("Asia/Almaty"))
print(dt.tzinfo)

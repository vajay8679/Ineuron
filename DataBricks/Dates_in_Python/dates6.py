#Handling timezone in Python
from datetime import datetime
import pytz

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

tz = pytz.timezone('America/New_York')
tz_time = datetime.now(tz)
new = tz_time.strftime("%m/%d/%Y, %H:%M:%S")
print("America : ",new)
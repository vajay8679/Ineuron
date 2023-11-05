from datetime import date, time, datetime

# date(year=2023, month=12, day=11)
# time(hour=11, minute=28, second=45)
# datetime(year=2023, month=12, day=11,hour=11, minute=28, second=45)


#Using dateutil to Add Time Zones to Python datetime

from dateutil import tz
from datetime import datetime
now = datetime.now(tz=tz.tzlocal())
# now #datetime.datetime(2023, 11, 5, 5, 11, 12, 208447, tzinfo=tzlocal())

now.tzname() # 'UTC'
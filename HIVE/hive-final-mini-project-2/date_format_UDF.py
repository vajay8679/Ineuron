import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip("\n\r")
    date_old_format = str(line)
    date_time_obj = datetime.strptime(date_old_format, '%d/%m/%Y')
    print(date_time_obj.date())
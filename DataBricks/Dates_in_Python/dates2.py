from datetime import datetime, timedelta


#Timedelta class
#This object allows us to add or subtract time or date to a specific date and time.

hour_delta = timedelta(hours=8)

today1 = datetime.now()

new_time = today1 + hour_delta

print(f'New Time after adding 8 hr is : {new_time}')


day_delta = timedelta(days=1)

new_day = today1 + day_delta

print(f'New Day after adding 1 day is : {new_day}')
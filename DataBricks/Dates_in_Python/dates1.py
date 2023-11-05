from datetime import date
from datetime import datetime

today1 = date.today()

# print(f'Todays Date is {today1}')

# print(f"Present Year:{today1.year}") 
# print(f"Present Month:{today1.month}") 
# print(f"Present Day:{today1.day}") 

# graduation_date = date(2025, 8, 22)


#for datetime difference

today2 = datetime.now()
graduation_date = datetime(2024,8,25,0,0,0)
diff_date = abs(graduation_date - today2)

print(f'No. of days left of graduation {diff_date}')


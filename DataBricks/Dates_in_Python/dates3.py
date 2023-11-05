import datetime

#If we want to convert the dates into readable strings, strftime() method is used.
today = datetime.datetime(2023,9,23,12,30,30)
read_date = today.strftime("%H:%M:%S %B %d %Y")

print(f'Date in readable format is : {read_date}') #Date in readable format is : 12:30:30 September 23 2023


#Parsing is used to convert a string into datetime format. strptime() is used to perform this. The parameters are date_string and format respectively.

# from datetime import datetime 
# print(datetime.strptime('26/5/2020', '%d/%m/%Y'))  #2020-05-26 00:00:00

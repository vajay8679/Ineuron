
Azure databricks

https://signup.azure.com/screen
https://github.com/vishalsingh17/BigDataAzureDatabricks/blob/main/Azure_Databricks.pdf
portal.azure.com

https://learn.microsoft.com/en-us/training/modules/explore-azure-databricks/01-introduction

https://learn.microsoft.com/en-us/azure/databricks/

https://azure.microsoft.com/en-gb/pricing/calculator/

https://community.cloud.databricks.com/login.html

https://learn.microsoft.com/en-us/azure/databricks/introduction/

https://community.cloud.databricks.com/?o=564081337477372#notebook/872117828706425/command/872117828706426

https://community.cloud.databricks.com/?o=564081337477372#
vajay8679@gmail.com
Vajay8679@



in notebook -> select python-> cluster




pip install databricks-cli
databricks --help
databricks configure --token   #configure with ur workspace
databricks fs --help
databricks fs ls
databricks fs ls dbfs:/FileStore/tmp



# if loading JSON string  then use 'json.loads()' and if loading file then use 'json.load()'
# if show JSON string in petty printing json then 'json.dumps(dictionary, indent = 4)' and if writing file then use 'json.dump(dictionary, output_file)'

# For encoding, we use json.dumps() and for decoding, we’ll use json.loads(). So it is obvious that the dumps method will convert a python object to a serialized JSON string and the loads method will parse the Python object from a serialized JSON string.

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.



# extract specific parts of a JSON structure based on a search query.

import json
import jmespath
json_string = '{"numbers": [1, 2, 3], "car": {"model": "Model X", "year": 2022}}'
json_data = json.loads(json_string) 
# Accessing nested JSON 
name = jmespath.search('car.model', json_data) # Result: Model X 
# Taking the first number from numbers 
first_number = jmespath.search('numbers[0]', json_data)  # Result: 1


# In JSON, keys must be strings, written with double quotes:

{"name":"John"}



https://jsonplaceholder.typicode.com/posts/1
https://jsonplaceholder.typicode.com/users/1/todos



https://punkapi.com/documentation/v2
https://api.punkapi.com/v2/beers/random


skipinitialspace=True is used to remove extra space from csv file in -> csv.reader(csvfile, skipinitialspace=True)

quoting=csv.QUOTE_ALL  in csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True) for -> ""
# csv.QUOTE_ALL specifies the reader object that all the values in the CSV file are present inside quotation marks.


import csv
csv.register_dialect('myDialect',
                     delimiter='|',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

with open('office.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        print(row)


# Instead of passing three individual formatting patterns, let's look at how to use dialects to read this file.



date.today() creates a datetime.date instance with the current local date.
datetime.now() creates a datetime.datetime instance with the current local date and time.
datetime.combine() combines instances of datetime.date and datetime.time into a single datetime.datetime instance.


https://realpython.com/python-datetime/


# The strftime() method is defined under classes date, datetime and time. The method creates a formatted string from a given date, datetime or time object.

# The strptime() method creates a datetime object from a given string (representing date and time). 

# Handling timezone in Python
from datetime import datetime
import pytz
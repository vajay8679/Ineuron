import pymongo

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Database Name
dataBase = client["neurolabDB"]

# Collection  Name
collection = dataBase['Products']

# Sample data
d = {'companyName': 'iNeuron',
     'product': 'Affordable AI',
     'courseOffered': 'Machine Learning with Deployment'}

# Insert above records in the collection
rec = collection.insert_one(d)

# Lets Verify all the record at once present in the record with all the fields
all_record = collection.find()

# Printing all records present in the collection
for idx, record in enumerate(all_record):
     print(f"{idx}: {record}")



#today class

import pymongo

#connect with the mongodb
dbConn = pymongo.MongoClient("mongodb://localhost:27017/")

dbname='ineuron'

db=dbConn[dbname]

collection_name='mongo_demo'

collection=db[collection_name]

my_row = {'Serial No': '9998',
 'GRE Score': '337',
 'TOEFL Score': '118',
 'University Rating': '4',
 'SOP': '4.5',
 'LOR': '4.5',
 'CGPA': '9.65',
 'Research': '1',
 'Chance of Admit': '0.92'}


col=collection.insert_one(my_row)

my_rows=[
    {'Serial No': '9998',
 'GRE Score': '337',
 'TOEFL Score': '118',
 'University Rating': '4',
 'SOP': '4.5',
 'LOR': '4.5',
 'CGPA': '9.65',
 'Research': '1',
 'Chance of Admit': '0.92'},

 {'Serial No': '1000',
 'GRE Score': '310',
 'TOEFL Score': '100',
 'University Rating': '2',
 'SOP': '4.2',
 'LOR': '3.5',
 'CGPA': '9.00',
 'Research': '0',
 'Chance of Admit': '0.70'}] 

collection.insert_many(my_rows)

res=collection.find()

for i in res:
    print(i)

#for getting interseted if
col.inserted_id
col.inserted_id

#for getting limited record
result_total=collection.find({}).limit(2)

# without curly braces you won't be able to get single record(record[1] it won't work here)
#you will have to add curly baces.
result=collection.find()
record=collection.find()

result=collection.find({},{'GRE Score','TOEFL Score'})
my_rows = [
{'Serial No': '9997',
 'GRE Score': '337',
 'TOEFL Score': '118',
 'University Rating': '4',
 'SOP': '4.5',
 'LOR': '4.5',
 'CGPA': '9.65',
 'Research': '1',
 'Chance of Admit': '0.92'},
  {
    'Serial No': '9996',
 'GRE Score': '336',
 'TOEFL Score': '118',
 'University Rating': '4',
 'SOP': '4.5',
 'LOR': '4.5',
 'CGPA': '9.6',
 'Research': '0',
 'Chance of Admit': '0.92'},
  {
    'Serial No': '9995',
 'GRE Score': '337',
 'TOEFL Score': '118',
 'University Rating': '4',
 'SOP': '4.5',
 'LOR': '4.5',
 'CGPA': '9.5',
 'Research': '1',
 'Chance of Admit': '0.92'},
  {
    'Serial No': '9994',
 'GRE Score': '334',
 'TOEFL Score': '119',
 'University Rating': '4',
 'SOP': '4.5',
 'LOR': '4.5',
 'CGPA': '9.4',
 'Research': '1',
 'Chance of Admit': '0.92'},
  {
    'Serial No': '9993',
 'GRE Score': '337',
 'TOEFL Score': '118',
 'University Rating': '4',
 'SOP': '4.5',
 'LOR': '4.5',
 'CGPA': '9.65',
 'Research': '1',
 'Chance of Admit': '0.92'}

]
#task for today's session
import pandas as pd

dataframe=pd.read_csv("https://raw.githubusercontent.com/vigneshk/Admission-Dataset/master/Admission.csv")

"""
1. create a database iNeuron
2. create a collection Addmision_details
3. you have to dump this dataframe to mongodb collection.

"""

#google form for submission

https://forms.gle/Cw7552m8TWTyauG28

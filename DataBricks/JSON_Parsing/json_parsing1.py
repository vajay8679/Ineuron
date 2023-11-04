#writing json to a file in python

import json

dict ={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}

with open('sample.json','w') as output_file:
    json.dump(dict,output_file)
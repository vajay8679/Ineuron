
import json

#Encoding (Serialization): Converting a Python object to a JSON string.

data = {"name": "John", "age": 30, "city": "New York"}
json_data = json.dumps(data)
print(json_data)


#Decoding (Deserialization): Converting a JSON string into a Python object.

json_data = '{"name": "John", "age": 30, "city": "New York"}'
data1 = json.loads(json_data)
print(data1)
print(data1['name'])


#Reading JSON from a File:

with open("data.json", "r") as file:
    data = json.load(file)



#Writing JSON to a File:
data = {"name": "John", "age": 30, "city": "New York"}
with open("data1.json", "w") as file:
    json.dump(data, file)

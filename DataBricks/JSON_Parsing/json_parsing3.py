import json

json_string ='{"numbers": [1, 2, 3], "car": {"model": "Model X", "year": 2022}}'

json_data = json.loads(json_string) 

# Accessing JSON array elements using array indexing 
print(json_data['numbers'][0])  # Output: 1 
# Accessing JSON elements using keys 
print(json_data['car']['model'])  # Output: Model X


#adding an element json_data

json_data['color'] = 'red'

print(json_data)

#modifying an element in json_data

json_data['car']['year'] = '2023'

print(json_data)
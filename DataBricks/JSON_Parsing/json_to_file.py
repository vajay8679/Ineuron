
import json

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32,
"Profession": None
}

with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)
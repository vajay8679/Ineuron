import json 

# A basic python dictionary 
py_object = {"c": 0, "b": 0, "a": 0} 

# Encoding 
json_string = json.dumps(py_object) 
print(json_string) 
print(type(json_string)) 

# Decoding JSON 
py_obj = json.loads(json_string) 
print() 
print(py_obj) 
print(type(py_obj)) 




# output

# {"c": 0, "b": 0, "a": 0}
# <class 'str'>

# {'c': 0, 'b': 0, 'a': 0}
# <class 'dict'>
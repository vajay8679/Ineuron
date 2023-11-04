import json

json_string = '{"model": "Model X", "year": 2022}'

res = json.loads(json_string)

more_json_string = '{"model": "Model S", "color": "Red"}'
res1 = json.loads(more_json_string)

#updating or adding another approach
res.update(res1)

print(res)


#deleteing 

# del res['year']


if 'year' in res: 
    del res['year'] 
else: 
    print('Key not found') 

# or wrapping the del operation with a try/catch
# json_string = '{"model": "Model X", "year": 2022}'
# json_data = json.loads(json_string) 
# try: 
#     del json_data['year']
# except KeyError: 
#     print('Key not found')


print(res)
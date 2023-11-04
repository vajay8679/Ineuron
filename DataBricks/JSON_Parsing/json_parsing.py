import json

#opening file
f = open('data.json',)
res = json.load(f)

# for i in res['emp_details']:
# 	print(i)

# print(res['emp_details'][0])

print(res['emp_details'][0]['emp_name'])



#closing file
f.close()
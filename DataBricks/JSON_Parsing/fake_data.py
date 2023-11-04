import json

with open('fake_data.json', 'r' ) as file:
    data = json.load(file)

    # print(data[0])
    # print(data[0]['username'])
    # print(data[0]['email'])
    # print(data[0]['address']['zipcode'])

    # name = data[0]['username']
    # email = data[0]['email']
    # zipcode = data[0]['address']['zipcode']

    # person = {
    #     'name' : name,
    #     'email' : email,
    #     'zipcode' : zipcode
    # }

    person_list = []
    for item in data:
        name = item['username']
        email = item['email']
        zipcode = item['address']['zipcode']

        person = {
            'name' : name,
            'email' : email,
            'zipcode' : zipcode
        }
    
        person_list.append(person)
        
print(person_list)
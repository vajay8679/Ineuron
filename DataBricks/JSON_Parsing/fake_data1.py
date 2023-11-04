import json
import requests

res = requests.get('https://api.punkapi.com/v2/beers/random')

response_data = json.loads(res.text)

# print(response_data)
# print(response_data[0]['name'])

# print(response_data[0]['name'],response_data[0]['tagline'],response_data[0]['abv'])



# print(response_data1[0]['name'])
# print(len(response_data1))

beer_data = []
for beer in response_data1:
    name = beer['name']
    tagline = beer['tagline']
    abv = beer['abv']

    beer_res = {
        'name' : name,
        'tagline' : tagline,
        'abv' : abv
    }

    beer_data.append(beer_res)

print(beer_data)
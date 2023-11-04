#fake Api data dynmically data

import json
import requests
from random import randint

food_choice = input("please enter food of your choice : ")
res1 = requests.get(f'https://api.punkapi.com/v2/beers?food={food_choice}')

response_data1 = json.loads(res1.text)

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

# print(beer_data)

value = randint(0,len(beer_data))

new_item = beer_data[value]
# print(new_item)



new_item_name = new_item['name']
new_item_tagline = new_item['tagline']
new_item_abv = new_item['abv']

print(f'You should try {new_item_name},{new_item_tagline},{new_item_abv} %')
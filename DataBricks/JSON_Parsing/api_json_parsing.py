#fake api url request

import json
import requests

res = requests.get('https://jsonplaceholder.typicode.com/posts/1')

response_data = json.loads(res.text)

print(response_data)
print(response_data['title'])
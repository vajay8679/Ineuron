#Advanced JSON Operations:

import json

data = {
    "employees": [
        {"name": "John", "age": 30},
        {"name": "Alice", "age": 25}
    ]
}


json_data = json.dumps(data, indent=2)


print(json_data)
import json

with open('sample.json','r') as file_open:
    f_file = json.load(file_open)

    # print(f_file)

    #prettyfy json 

    f_pretty = json.dumps(f_file,indent=4,sort_keys=True)
    print(f_pretty)
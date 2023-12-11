import json

with open('Python-task.json','r') as json_file:
    json_reader = json.load(json_file)

    hotel_name = json_reader['assignment_results'][0]['hotel_name']
    net_price_data = json_reader['assignment_results'][0]['net_price']

    # Convert price value to floats for comparison
    price = {key:float(value) for key,value in net_price_data.items()}

    room_name = "" #Initialize room_name
    lowest_price = float('inf')  # Initialize with positive infinity

    for key, value in price.items():
        if value < lowest_price:
            lowest_price = value
            room_name = key

    print(f'Hotel Name  is : {hotel_name}')
    print(f'Room name is : {room_name} &  lowest price is : {lowest_price} from net_price. ')

#output
# Hotel Name  is : Home2 Suites By Hilton San Francisco Airport North
# Room name is : King Studio Suite - Non Smoking &  lowest price is : 90.0 from net_price. 


    
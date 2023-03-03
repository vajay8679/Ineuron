import json
import random 

name_list = ["Ajay","Amit","Sumit","Raja","Ravi","Hariom","Raj"]
age_list = [28,25,23,29,24,22,21]
salary_list = [1000,2000,3000,4000,5000,6000,7000]

def lambda_handler(event, context):
    # TODO implement
    random_index = random.randint(0,6)
    mock_data = {}
    mock_data['emp_name'] = name_list[random_index]
    mock_data['emp_age'] = age_list[random_index]
    mock_data['emp_list'] = salary_list[random_index]
    return mock_data
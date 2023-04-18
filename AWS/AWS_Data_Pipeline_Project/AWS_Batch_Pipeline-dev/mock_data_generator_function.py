import json
import random 

# s3_client = boto3.client('s3')
name_list = ['Ajay','Amit','Sumit','Raja','Ravi','Hariom']
age_list = [27,24,23,28,25,22]
salary_list = [1000,2000,3000,4000,5000,6000]

def lambda_handler(event, context):
    print(event)
    random_list = random.randint(0,5)
    
    # TODO implement
    return {
            'emp_name': name_list[random_list],
            'emp_age': age_list[random_list],
            'emp_salary': salary_list[random_list]
           }

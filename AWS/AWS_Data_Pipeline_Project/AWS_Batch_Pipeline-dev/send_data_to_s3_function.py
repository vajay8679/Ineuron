import json
import boto3
import datetime

def lambda_handler(event, context):
    print(event['responsePayload'])
    employee_data = event['responsePayload']
    BUCKET_NAME = 'employee-projects-json'
    current_epoch_time = datetime.datetime.now().timestamp()
    
    print("Start Data Write in S3")
    
    s3 = boto3.resource('s3')
    s3Object = s3.Object(BUCKET_NAME,f"index/{str(current_epoch_time)}_employee_data.json")
    s3Object.put(
        Body = (bytes(json.dumps(employee_data).encode('UTF-8')))
    )
    
    print("Data Write Successfull in S3")
import json
import boto3
import datetime

def lambda_handler(event, context):
    print(event['responsePayload'])
    employee_data = event['responsePayload']
    BUCKET_NAME = "employee-project-sample-data"
    current_epoch_time = datetime.datetime.now().timestamp()

    print("Start Data Write in S3")
    s3 = boto3.resource('s3')
    s3object = s3.Object(BUCKET_NAME,f"inbox/{str(current_epoch_time)}_employee_data.json")
    s3object.put(
            Body=(bytes(json.dumps(employee_data).encode('UTF-8')))
    )
    print("Data write Successfull in S3")

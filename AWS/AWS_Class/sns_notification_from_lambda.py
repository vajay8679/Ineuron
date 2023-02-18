import boto3
import pandas as pd
from io import BytesIO
import json

# s3_client = boto3.client('s3')
client = boto3.client('sns')
snsArn = "arn:aws:sns:ap-south-1:566373416292:batch1-sns-topic"

def lambda_handler(event, context):
    message = "Hi,This is test message from Lambda !!!"
    
    response = client.publish(
        TargetArn=snsArn,
        Message=message,
        MessageStructure='text'
    )
    print(response)

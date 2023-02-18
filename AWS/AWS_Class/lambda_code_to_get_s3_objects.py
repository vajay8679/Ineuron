import json
import boto3
s3 = boto3.resource('s3')

def lambda_handler(event, context):
    # TODO implement
    bucket = s3.Bucket('batch1s3bucket')
    print(bucket.objects.all())
    print("=========================")
    for obj in bucket.objects.all():
        key = obj.key
        print(key)

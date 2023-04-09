import boto3
import pandas as pd
from io import BytesIO

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    print(event)
    try:
        bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        s3_file_name = event["Records"][0]["s3"]["object"]["key"]
        print(bucket_name)
        print(s3_file_name)
        resp = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
        print(resp['Body'])
        df_s3_data = pd.read_csv(resp['Body'], sep=',')
        print(df_s3_data.head())
    except Exception as err:
        print(err)

import boto3
import csv

# Define your AWS access key ID and secret access key
aws_access_key_id = 'AKIA2GM5ZBDD4MPDH6NL'
aws_secret_access_key = 'hKzlFKkNif7UEWFGpJ49/rSM32pOGieVRcc9axWz'

# Define your S3 bucket name
bucket_name = 'project-nee/raw_data'

# Define a list of file paths for the CSV files to upload
file_paths = ['employee.csv', 'employee1.csv', 'employee2.csv']

# Create an S3 client with authentication credentials
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Loop over the list of file paths and upload each CSV file to the S3 bucket
for file_path in file_paths:
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            # Define the S3 object key for the CSV file (using the row index as a suffix)
            object_key = f'{file_path.split("/")[-1]}_{i}.csv'

            # Upload the CSV file to the S3 bucket
            s3.upload_file(file_path, bucket_name, object_key)

            print(f'Uploaded {object_key} to {bucket_name}.')
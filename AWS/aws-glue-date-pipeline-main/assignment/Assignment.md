1. Create a AWS Lambda function to read from any open source API such https://rapidapi.com/ and store it into s3 bucket.
2. Create a redshift table to store record of s3 files data.
3. Crate a AWS Glue Job to move data from s3 bucket to  Amazon Redshift.
4. Schedule AWS Lambda function to download data automatically on specific interval.
5. Schedule AWS Glue Job to move data from s3 to Redshift.


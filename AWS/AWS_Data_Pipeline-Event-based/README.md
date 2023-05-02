#################################################
           Event-Based-AWS-Data-Pipeline
#################################################

1. https://s3.console.aws.amazon.com/s3/buckets/project-digi?region=ap-south-1&tab=properties
    #create S3 Bucket
    Bucket Name - project-digi 
   
    created 4 objects - 1.raw_data
                        2.cureated_data
                        3.athena_output
                        4.token

create Event notification with name in properties section of 'project-digi' bucket - 'project-digi-event-lambda'
Event types - Put, Post
Filters - 'token'
Destination type - 'Lambda function'
Destination - 'project_digi_function'
Enter Lambda function ARN - 'arn:aws:lambda:ap-south-1:700947433671:function:project_digi_function'


2. https://ap-south-1.console.aws.amazon.com/lambda/home?region=ap-south-1#/functions/project_digi_function?newFunction=true&tab=code
    #create a function in Lambda
    function name - 'project_digi_function'

3. https://ap-south-1.console.aws.amazon.com/gluestudio/home?region=ap-south-1#/editor/job/digi-job/script
    #created Glue Job
    Job Name - 'digi-job'
    job bookmarks -  Enable

4. https://ap-south-1.console.aws.amazon.com/glue/home?region=ap-south-1#/v2/data-catalog/crawlers/view/digi-crawler
    #create AWS Glue Crawler
    Crawler name - 'digi-crawler'

5. https://ap-south-1.console.aws.amazon.com/glue/home?region=ap-south-1#/v2/data-catalog/databases/view/project-digi-db?catalogId=700947433671
    #create db
    db name - 'project-digi-db'

6. https://ap-south-1.console.aws.amazon.com/glue/home?region=ap-south-1#/v2/etl-configuration/workflows/view/project-digi-wk
    #create workflow
    workflow name - 'project-digi-wk'

    1.trigger name - project-digi-job-trigger 
      Trigger type - ON_DEMAND

    2.job Name - digi-job
      Triggered by - project-digi-job-trigger

    3.trigger name - project-digi-crawler-trigger
      Trigger type - CONDITIONAL
      Trigger logic -Start after ANY watched event

    4.Crawler Name - digi-crawler

7. https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/roles/details/AWSGlueServiceRole-digi?section=permissions
    #while creating crawler it ask for create IAM role 
    Role - 'AWSGlueServiceRole-digi'
    #Attach policies in Role
    'AWSGlueServiceRole-digi-EZCRC-s3Policy'
    'AmazonS3FullAccess'
    'AWSGlueServiceRole'
    'AdministratorAccess'


8. https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1&state=hashArgs%23%2Froles%2Fdetails%2Fproject_digi_function-role-l45r21wj%3Fsection%3Dpermissions#/roles/details/project_digi_function-role-l45r21wj?section=permissions

    #while creating Lambda Function it creates IAM role 
    IAM Role - 'project_digi_function-role-l45r21wj'
    #Attach policies in Role 
    AdministratorAccess

9. https://ap-south-1.console.aws.amazon.com/athena/home?region=ap-south-1#/query-editor/history/bb92f281-0ecc-4063-a0e5-27f0fb6c56d7
    
    in Athena in Query Editor 
    Data source - AWSDataCatalog
    Database - project-digi-db

    in setting
    Query result location - 's3://project-digi/athena_output/'

    

Description -

First we will create event based 'project_digi_function' then create S3 Bucket (project-digi) and create 4 folders inside this bucket with name - raw_data,cureated_data,athena_output,token and then in 'properties' section go to 'event notification' in bucket and create Event notifications with name 'project-digi-event-lambda' with event type -Put,Post
then create Glue Job - 'digi-job' and enable job bookmarks and then create crawler with name (digi-crawler) and while creating crawler create db - (project-digi-db) and then create workflow with job-trigger and crawler-trigger.

Now upload parquet file in S3 bucket in raw_data folder then after it we will upload token file in token folder then after it our workflow will start running and then after workflow will run successfully then we can check in Athena by selecting Data source - AWSDataCatalog and Database - project-digi-db and in setting  select 'Query result location' -> 's3://project-digi/athena_output/' and then run query then we will get data in csv format in athena_output folder, 
repeat same process again then we will get incremental data. 

Thats how our Event based AWS Data pipeline works.







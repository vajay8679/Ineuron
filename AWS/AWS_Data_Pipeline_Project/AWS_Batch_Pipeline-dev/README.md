#################################################
            Batch-Data-Pipeline
#################################################

1. https://ap-south-1.console.aws.amazon.com/events/home?region=ap-south-1#/eventbus/default/rules/mock_data_generator_trigger
    #create EventBridge
    Amazon EventBridge > Schedules > mock_data_generator_trigger 
    Rule - 'mock_data_generator_trigger'
    select target -> lambda -> mock_data_generator_function

2. https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/create/function
    #create a function in Lambda
    (1) function name - 'mock_data_generator_function'
    (2) function name - 'send_data_to_s3_function'

3. https://us-east-1.console.aws.amazon.com/iamv2/home?region=ap-south-1#/roles/details/send_data_to_s3_function-role-r96cbkcp?section=permissions
    #check Role in IAM
    Role - 'send_data_to_s3_function-role-r96cbkcp'
    #Attach policies in Role - 'AmazonS3FullAccess'

4. https://s3.console.aws.amazon.com/s3/buckets/employee-projects-json?region=ap-south-1&tab=objects
    #create s3 bucket
    bucket name - 'employee-projects-json'
    object inside bucket - 'index'

5. https://ap-south-1.console.aws.amazon.com/glue/home?region=ap-south-1#/v2/data-catalog/crawlers/view/employee_json_data_crawler
    #create crawlers
    crawler name - 'employee_json_data_crawler'
    classifierer - 'employee_json_data_parser_new'
    Json path in classifierer - $.emp_name,$_emp_age,$.emp_salary

6. https://ap-south-1.console.aws.amazon.com/glue/home?region=ap-south-1#/v2/data-catalog/databases/view/employee_data_db?catalogId=700947433671
    #create database
    db_name - 'employee_data_db'

7. https://ap-south-1.console.aws.amazon.com/gluestudio/home?region=ap-south-1#/editor/job/employee_data_ingestion_to_dynamo/script
    #create Glue Job
    job Name - 'employee_data_ingestion_to_dynamo'

8. https://us-east-1.console.aws.amazon.com/iamv2/home?region=ap-south-1#/roles/details/AWSGlueServiceRole-test?section=permissions
    while creating crawler it ask for create IAM role 
    IAM Role - 'AWSGlueServiceRole-test'
    #Attach policies in Role 
    AWSGlueServiceRole-test-EZCRC-s3Policy
    AmazonDynamoDBFullAccess
    AmazonRedshiftFullAccess
    AmazonS3FullAccess	
    AWSGlueServiceRole	
    AWSGlueConsoleFullAccess

9. https://ap-south-1.console.aws.amazon.com/dynamodbv2/home?region=ap-south-1#tables
    #create dynamodb table
    table name - 'employee_data'

Description -

First we will create scheduled based eventBridge 'mock_data_generator_trigger' then while selecting target we will create lambda function 'mock_data_generator_function' which write mock data then create destination lambda function 'send_data_to_s3_function' that will receive data from 'mock_data_generator_function' and send data to s3 bucket 'employee-projects-json/index' then create crawler 'employee_json_data_crawler' while creating crawler we have to create classifier 'employee_json_data_parser_new'  because we are saving data in JSON format and we have to create database with name 'employee_data_db' and then run crawler so it will create infer schema and and it will create metadata table inside 'employee_data_db' with name 'json_index' then we have to create Glue Job and we have to make 'Job bookmark -> Enable' in job details then inside dynamodb we have to create table with name 'employee_data'.

Once we Enable EventBridge based on our scheduled time Our Batch_data_pipeline will start working.



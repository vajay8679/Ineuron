#################################################
           Scheduled-Based-AWS-Data-Pipeline
#################################################

1. https://s3.console.aws.amazon.com/s3/buckets/ajay-bucket1?region=ap-south-1&tab=objects
    #create S3 Bucket
    Bucket Name - ajay-bucket1 
   
    created 2 objects - 1.ajay-input-athena
                        2.ajay-output-athena

2. https://ap-south-1.console.aws.amazon.com/events/home?region=ap-south-1#/eventbus/default/rules/event-bridge-rule-for-glue
    #create a  Scheduled based EventBridge Rule
    Rules name - 'event-bridge-rule-for-glue'
    Schedule pattern - 44 12 * * ? *
    Select a target - Glue workflow
    Glue workflow name - glue-job-workflow
    Use existing role



3. https://ap-south-1.console.aws.amazon.com/gluestudio/home?region=ap-south-1#/editor/job/test-job/script
    #created Glue Job
    Job Name - 'test-job'
    job bookmarks -  Enable

4. https://ap-south-1.console.aws.amazon.com/glue/home?region=ap-south-1#/v2/data-catalog/crawlers/view/ajay1
    #create AWS Glue Crawler
    Crawler name - 'ajay1'
    Data Source - s3://ajay-bucket1/ajay-input-athena/
    Parameter- Recrawl all
    Schedule - on demand

5. https://ap-south-1.console.aws.amazon.com/glue/home?region=ap-south-1#/v2/data-catalog/databases/view/ajay1-test?catalogId=700947433671
    #create db
    db name - 'ajay1-test'

6. https://ap-south-1.console.aws.amazon.com/glue/home?region=ap-south-1#/v2/etl-configuration/workflows/view/glue-job-workflow
    #create workflow
    workflow name - 'glue-job-workflow'

    1.trigger name - glue_crawler_trigger
      Trigger type - EVENT

    2.Crawler Name - ajay1
      Triggered by - glue_crawler_trigger

    3.trigger name - glue_job_trigger
      Trigger type - CONDITIONAL
      Trigger logic -Start after ANY watched event

    4.Job Name - test-job
      Triggered by - glue_job_trigger

7. https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/roles/details/b1-s3-glue-role?section=permissions

    #while creating Crawler creates IAM role 
    IAM Role - 'b1-s3-glue-role'
    #Attach policies in Role 
    AmazonS3FullAccess
    AWSGlueServiceRole
    AdministratorAccess

8. https://ap-south-1.console.aws.amazon.com/athena/home?region=ap-south-1#/query-editor/history/ba93261f-64cc-4a22-8786-0fec1b06cea8
  
    in Athena in Query Editor 
    Data source - AWSDataCatalog
    Database - ajay1-test
    in setting
    Query result location - 's3://ajay-bucket1/ajay-output-athena/'

9. https://s3.console.aws.amazon.com/s3/buckets/ajay-bucket1?region=ap-south-1&prefix=ajay-output-athena/&showversions=false
    
    check output in bucket :- 
    ajay-bucket1 > ajay-output-athena


   
    

Description -

First we will create S3 Bucket - 'ajay-bucket1' and created 2 objects - 1.ajay-input-athena 2.ajay-output-athena and then created EventBridge Rule with name - 'event-bridge-rule-for-glue' and then created Glue Job with name - 'test-job' with job bookmarks - Enable and then create a crawler with Crawler name - 'ajay1' and  Data Source - 's3://ajay-bucket1/ajay-input-athena/' and
Parameter- 'Recrawl all' and Schedule - 'on demand' and while creating crawler create DB with name 'ajay1-test' and created IAM role with name - 'b1-s3-glue-role' and attached policies then create workflow with name 'glue-job-workflow'.



When we will insert csv file inside bucket in folder 'ajay-input-athena' and we have scheduled Workflow (Ex. every 2min or every hr) then our Workflow will start running and then after succesfull execution of workflow we can check in Athena by selecting database and while running query we can see Athena output data inside bucket inside folder 'ajay-output-athena'.

Thats how we can get incremental data based on our scheduled timing.

Thats how our Scheduled based Data Pipeline will work.




#################################################
            Batch-Data-Pipeline
#################################################


#create a function in Lambda
https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/create/function
1. function name - 'mock-data-generator'

2. function name - send-data-to-s3


#check Role in IAM
https://us-east-1.console.aws.amazon.com/iamv2/home?region=ap-south-1#/roles/details/send-data-to-s3-role-xzj1fcu8?section=permissions
IAM > Roles >send-data-to-s3-role-xzj1fcu8

Role - 'send-data-to-s3-role-xzj1fcu8'

#Attach policies in Role -
'AmazonS3FullAccess'



https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions/send-data-to-s3?tab=configure



#create s3 bucket
bucket name - 'employee-project-sample-data'


#add destination
https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/functions/mock-data-generator/create/destination?tab=code

Destination -> sendDataToS3



#check in cloud watch part
https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252FSendDataToS3




#created rule in Event bridge
https://us-east-1.console.aws.amazon.com/events/home?region=us-east-1#/rules

Amazon EventBridge > Schedules > mock-data-generator-trigger
Rule - 'mock-data-generator-trigger'





#cloud watch - mock-data-generator
CloudWatch > Log groups > /aws/lambda/mock-data-generator 
https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252Fmock-data-generator

#cloud watch - SendDataToS3
CloudWatch > Log groups > /aws/lambda/SendDataToS3 

https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252FSendDataToS3






#####################################################################
https://ap-south-1.console.aws.amazon.com/glue/home?region=ap-south-1#/v2/data-catalog/crawlers

create crawlers


create db in glue


go in dynamodb
create table




https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html
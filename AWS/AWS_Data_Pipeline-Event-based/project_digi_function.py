import boto3

def lambda_handler(event, context):

    glue = boto3.client('glue')
    workflow_name = 'project-digi-wk'
    response = glue.start_workflow_run(Name=workflow_name)
    return response
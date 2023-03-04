from collections import namedtuple
import os




class EnvironmentVariable:

    def __init__(self):
        try:

            #redshift environment variable
            redshift_user_name= os.getenv("REDSHIFT_USER_NAME")
            redshift_passowrd = os.getenv("REDSHIFT_PASSWORD")
            redshift_uri = os.getenv("REDSHIFT_JDBC_URL").replace("<user_name>",redshift_user_name).replace("<password>",redshift_passowrd)
            self.redshift = (namedtuple("redshift",["uri","user_name","password"])
            (uri=redshift_uri,user_name=redshift_user_name,password=redshift_passowrd,))

            #aws realted detail
            access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
            secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
            temp_bucket_name = os.getenv("TEMP_BUCKET_NAME") #this bucket will be used by redshift during read and write
            self.aws = (namedtuple("aws",["access_key_id","secret_access_key","temp_bucket_name"])
            (access_key_id=access_key_id,secret_access_key=secret_access_key,temp_bucket_name=temp_bucket_name))
        except Exception as e:
            raise e



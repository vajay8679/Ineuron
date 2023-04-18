import os

import pymongo

from lambda_function_code import COLLECTION_NAME, DATABASE_NAME, client,lambda_handler
import datetime



if __name__ == "__main__":
    print(lambda_handler("a","b"))

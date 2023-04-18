To create zip file for aws lambda function 

use below commadn

```commandline
pip install --platform manylinux2014_x86_64 --target=<folder_name> --implementation cp --python 3.9 --only-binary=:all: --upgrade <lib1> <lib2>
```

```
pip install --platform manylinux2014_x86_64 --target=lambda_function_code --implementation cp --python 3.9 --only-binary=:all: --upgrade pymongo[srv] requests boto3
```
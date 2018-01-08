import boto3
#import botocore

# Make sure you've created a test configuration named 'lambda'
# in your ~/.aws/credentials file that has sufficient permissions
# to interact with S3.
# Invoke the test like this:
# 'export AWS_PROFILE='lambda' ;python boto3_s3_upload_download.py'

# Configs
BUCKET_NAME = 'zappa-4mp57o9mq'
KEY_NAME = 'secret_key.pem'

# Get the service client
s3_client = boto3.client('s3')

# Upload a key file
s3_client.upload_file('secret_key.pem', BUCKET_NAME, KEY_NAME)

# Download object at bucket-name with key-name to file-like object
s3_resource = boto3.resource('s3')
secret_key_obj = s3_resource.Object(BUCKET_NAME, KEY_NAME)
secret_key_text = secret_key_obj.get()['Body'].read().decode('utf-8')

print('secret_key_text: ', secret_key_text)

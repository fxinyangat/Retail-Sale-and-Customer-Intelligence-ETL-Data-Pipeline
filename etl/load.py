import boto3
import os

def load_to_s3(file_path, bucket_name, s3_key):
    s3 = boto3.client("s3")
    s3.upload_file(file_path, bucket_name,s3_key)
    print(f"Uploaded to s3://{bucket_name}/{s3_key}")
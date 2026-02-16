import boto3 
from dotenv import load_dotenv 
import os 
import logging 
from datetime import datetime

load_dotenv() 

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
bucket_name = os.getenv("bucket_name")



# data_list =  [] 

# path = r"C:\Users\ThomasDuong\Documents\GitHub\bikepoint_project\data"

# for root, dirs, files in os.walk(path):
#     for file in files:
#         print(file) 
#         data_list.append(file)

# print(data_list)



# filepath = "data/2026-01-07 16-17-57.json"

# s3_client = boto3.client(
#     's3'
#     , aws_access_key_id = AWS_ACCESS_KEY
#     , aws_secret_access_key = AWS_SECRET_KEY
# )

# s3_filename = "2026-01-07 16-17-57.json"

# s3_client.upload_file(filepath, bucket_name, s3_filename)

filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

log_filename = f"logs/{filename}.log"

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_filename
)

logger = logging.getLogger()

data_list =  [] 

path = r"C:\Users\ThomasDuong\Documents\GitHub\bikepoint_project\data"

for root, dirs, files in os.walk(path):
    for file in files:
        full_path = os.path.join(root, file)
        data_list.append(full_path)

s3_client = boto3.client(
    's3'
    , aws_access_key_id = AWS_ACCESS_KEY
    , aws_secret_access_key = AWS_SECRET_KEY
)

if len(data_list) > 0:

    for filepath in data_list:

        s3_filename = os.path.basename(filepath)

        try:
            s3_client.upload_file(filepath, bucket_name, s3_filename)
            os.remove(filepath)
            logger.info(f"{s3_filename} upload successful at {filename}") 
        except Exception as e:
            print(f"Failed to upload {s3_filename}: {e}")
            logger.error(f"An error occurred with {s3_filename}: {e}")  
else:
    print("No files uploaded")
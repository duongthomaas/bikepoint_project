import os 
import boto3

def load_func(data_dir, access_key, secret_access_key, bucket_name, logger):
    '''
    Docstring for load_func
    To load json data from data_dir to S3 bucket
    
    :param data_dir: Description
    :param access_key: Description
    :param secret_access_key: Description
    :param bucket: Description
    :param logger: Description
    '''

    json_files = list(data_dir.glob('*.json'))

    if json_files:

    # data_list = []

    # path = r"C:\Users\ThomasDuong\Documents\GitHub\bikepoint_project\data"

    # for root, dirs, files in os.walk(path):
    #     for file in files:
    #         full_path = os.path.join(root, file)
    #         data_list.append(full_path)

    # if len(data_list) > 0:

        for filepath in json_files:

            s3_client = boto3.client(
                's3'
                , aws_access_key_id = access_key
                , aws_secret_access_key = secret_access_key
            )

            s3_filename = os.path.basename(filepath)

            try:
                s3_client.upload_file(filepath, bucket_name, s3_filename)
                # os.remove(filepath)
                logger.info(f"{s3_filename} upload successful at {data_dir}") 
            except Exception as e:
                print(f"Failed to upload {s3_filename}: {e}")
                logger.error(f"An error occurred with {s3_filename}: {e}")  
    else:
        print("No files uploaded")
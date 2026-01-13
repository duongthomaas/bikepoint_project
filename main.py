from datetime import datetime
from modules.logging import loggin_function
from modules.extract_func import extract_func
from modules.load_func import load_func
import os 
from dotenv import load_dotenv
from pathlib import Path 

load_dotenv() 

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
bucket_name = os.getenv("bucket_name")

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
url = "https://api.tfl.gov.uk/BikePoint"

extract_logger = loggin_function('extract', timestamp)

extract_func(url, 3, extract_logger, timestamp)

load_logger = loggin_function('extract', timestamp)

load_func(Path('data'), AWS_ACCESS_KEY, AWS_SECRET_KEY, bucket_name, load_logger)
import requests 
import os 
from datetime import datetime
import json
import time  
import logging 

logs_folder = 'logs'
if os.path.exists(logs_folder):
     pass
else:
    os.mkdir(logs_folder)

filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

log_filename = f"logs/{filename}.log"

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_filename
)

logger = logging.getLogger()

#Add the following to your script when you want logging to occur:
logger.debug("This is a debug message")    
logger.info("System working")            
logger.warning("Something unexpected")        
logger.error("An error occurred")             
logger.critical("Critical system error")

# Documentation here https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = "https://api.tfl.gov.uk/BikePoint"

no_of_tries = 3
count = 0

while count < no_of_tries:

    response = requests.get(url, timeout=10)

    response_code = response.status_code

    if response_code == 200:
        # Checks if this directory already exists, if not create one 
        folder = 'data'

        if os.path.exists(folder):
            pass
        else:
            os.mkdir(folder)
        
        response_json = response.json()


        filepath = f"{folder}/{filename}.json"

        try:
            with open(filepath, "w") as file:
                json.dump(response_json, file)
            print(f"Download successful at {filename}")
            logger.info(f"Download successful at {filename}") 
        except Exception as e:
            print(e)
            logger.error(f"An error occurred: {e}")   
        break 

    elif response_code > 499 or response_code < 200:
        print(response.reason)
        logger.warning(response.reason)  
        time.sleep(10)
        count +=1

    else: 
        print(response.reason)
        logger.error(response.reason) 
        break 
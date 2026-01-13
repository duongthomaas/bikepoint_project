import requests 
import os 
import json
import time  

def extract_func(url, no_of_tries, logger, timestamp):
    '''
    Docstring for extract_func

    To extract data from bikepoint API
    
    :param url: Description
    :param no_of_tries: Description
    :param logger: Description
    :param timestamp: Description
    '''

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


            filepath = f"{folder}/{timestamp}.json"

            try:
                with open(filepath, "w") as file:
                    json.dump(response_json, file)
                print(f"Download successful at {timestamp}")
                logger.info(f"Download successful at {timestamp}") 
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
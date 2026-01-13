import logging 
import os 
from datetime import datetime 

def loggin_function(prefix, timestamp):
    '''
    Docstring for loggin_function

    Set up the logs
    
    :param prefix: for the folder name for the logs
    :param timestamp: for the name of the log files
    '''
    
    dir = f"{prefix}_logs"
    os.makedirs(dir, exist_ok= True)

    log_filename = f"{dir}/{timestamp}.log"

    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_filename
    )

    return logging.getLogger()
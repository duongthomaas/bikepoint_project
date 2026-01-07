import requests 
import os 
from datetime import datetime
import json 

# Documentation here https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll
url = "https://api.tfl.gov.uk/BikePoint"

response = requests.get(url, timeout=10)

# print(response.status_code)

# Checks if this directory already exists, if not create one 
folder = 'data'

if os.path.exists(folder):
    pass
else:
    os.mkdir(folder)

if response.status_code == 200:
    response_json = response.json()
    print(f"Number of stations: {len(response_json)}")

else: 
    print(f"Request failed with status code {response.status_code}")
    print(response.text)

filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filepath = f"{folder}/{filename}.json"

with open(filepath, "w") as file:
    json.dump(response_json, file)

print(f"Download successful at {filename}")

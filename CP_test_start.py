'''
import requests
import json

# URL to fetch data from
url = "http://106.140.20.218/api/script/list/?node=cp-stts-srjo"

# Make a GET request
response = requests.get(url)

# Convert response to JSON format
data = response.json()  # Ensure the response is in JSON format

# Save JSON data to a file
with open("output.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

#print(type(data))
#print(data["campaign"][1]["value"][2])
#print(type(data))
#print(type(dict_data))

print("JSON data saved successfully!")



for i in range (1,3,1):
    for j in range(200):
        try:
            y = data["campaign"][i]["value"][j]
            if "Sanity" in y:
                print(y)
        except:
            break

'''






import requests
import json
import subprocess
import time
import CP_Automation 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import subprocess
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import random
import os
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



url = 'http://106.140.20.218/api/task/run/'



with open('test_config.json', 'r') as file:
    data = json.load(file)



headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36 Edg/133.0.0.0",
    "Content-Type": "application/json",
    "Referer": "http://106.140.20.218/overview?node=cp-stts-srjo"
}


x = requests.post(url, json=data, headers=headers)
print(x.status_code)
y = x.json()
print(type(y))
print(y["uid"])
uid = y["uid"]


time.sleep(3)

while True:
                
    test_url = f"http://106.140.20.218/api/task/item/?node=cp-stts-srjo&category=task&id={uid}"
    x = requests.get(test_url)
    y = x.json()
    result = y["verdict"]
    print(result)

    if result != "IN-PROGRESS":
        print("Starting Report....")
        time.sleep(15)
        CP_Automation.main()
        break



import time
from api_connector import get_data
from dbconfig import insert_data
from datetime import datetime 

current_time = datetime.now()

def task():
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

    result = insert_data(get_data())

    if result['success']:
        msg = f"Runned At: {timestamp} with status success \n"
    else:
        msg = f"Runned At: {timestamp} with status failed ' {result['error']['info']} ' \n"

    with open("C:\\Users\\lenovo\\Desktop\\currento/log.txt", 'a') as file:
        file.write(msg)

for i in range(100):
    print("running ...")
    task()
    time.sleep(60)

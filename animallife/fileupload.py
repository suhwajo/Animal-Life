import requests
import time
from datetime import datetime

now_time = datetime.now()

status = "eat"
time.sleep(3)

now_time2 = datetime.now()

files = {"video": open('C:\\Users\\이태경\\Desktop\\test.mp4', 'rb')}

params = {
            "title":"eat test2",
            "begin_timestamp":now_time,
            "end_timestamp":now_time2,
            "status":"eat",
            "user_id":"test@naver.com",
          }

res = requests.post('http://127.0.0.1:8000/upload_create/', data=params, files=files)
print(res.content)
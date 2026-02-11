import requests
import json
import os
from datetime import datetime

now = datetime.now()
target_id = now.minute + 1
url = f"https://jsonplaceholder.typicode.com/todos/{target_id}"

save_dir = "data"
if not os.path.exists(save_dir):
    os.makedirs(save_dir) 

file_path = os.path.join(save_dir, "서지혜_test.json")

response = requests.get(url)
if response.status_code == 200:
    new_data = response.json()
    
    data_list = []

    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data_list = json.load(f)
        except json.JSONDecodeError:
            pass 

    data_list.append(new_data)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)
        
    print(f"저장 완료: {file_path}")
else:
    print(f"요청 실패: Status Code {response.status_code}")
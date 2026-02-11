import requests
import json
import os
from datetime import datetime

now = datetime.now()
target_id = now.minute + 1
url = f"https://jsonplaceholder.typicode.com/todos/{target_id}"


response = requests.get(url)
if response.status_code == 200:
    new_data = response.json()
    
    file_path = "/tmp/서지혜_test.json"
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
        
    print(f"저장 완료: ID {target_id} 데이터를 {file_path}에 추가했습니다.")
else:
    print(f"요청 실패: Status Code {response.status_code}")
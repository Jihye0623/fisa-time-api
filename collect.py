import requests
import json
import os
import shutil 
from datetime import datetime

repo_file = "서지혜_test.json"      
tmp_file = "/tmp/서지혜_test.json"  

now = datetime.now()
target_id = now.minute + 1
url = f"https://jsonplaceholder.typicode.com/todos/{target_id}"

data_list = []
if os.path.exists(repo_file):
    try:
        with open(repo_file, "r", encoding="utf-8") as f:
            data_list = json.load(f)
            print(f"기존 데이터 {len(data_list)}개를 로드했습니다.")
    except:
        print("기존 파일이 비어있거나 깨져있어 새로 시작합니다.")


response = requests.get(url)
if response.status_code == 200:
    new_data = response.json()
    new_data['collected_at'] = str(datetime.now())
    data_list.append(new_data)

    with open(tmp_file, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)
        
    print(f"/tmp/ 디렉토리에 저장 완료: {tmp_file}")
    
else:
    print(f"요청 실패: Status Code {response.status_code}")
import requests
import os
import json


url = "https://jsonplaceholder.typicode.com"

dir_save = "json_file"
os.makedirs(dir_save, exist_ok=True)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()


    for item in data:
        file_path = os.path.join(dir_save, f"post_{item['id']}.json")
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(item, file, ensure_ascii=False, indent=4)

    print(f"Сохранено {len(data)} файлов в папку '{dir_save}'")
else:
    print("Ошибка")
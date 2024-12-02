import json


with open("charactersx`.json", "r") as file:
    data = json.load(file)  

    
for index, item in enumerate(data, start=1):
    output_file = f"item_{index}.json"
    with open(output_file, "w") as file:
        json.dump(item, file, indent=4)
    print(f"Создан файл: {output_file}")


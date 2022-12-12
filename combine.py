import json

res = []
for i in range(25):
    file_path = f"./ano/{i}.json"
    with open(file_path, 'r') as file:
        data = json.load(file)

        data['categories'][0]['id'] = i + 1
        res = res + data['categories']

for i in range(25):
    file_path = f"./ano/{i}.json"
    with open(file_path, 'r') as file:
        data = json.load(file)
        data['categories'] = res

        for j in data['annotations']:
            j['category_id'] = i + 1

    with open(file_path, 'w') as file:
        json.dump(data, file, indent="\t")
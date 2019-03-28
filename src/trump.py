import json

with open('trump.json', encoding="utf8") as json_file:  
    data = json.load(json_file)
    
for tweet in range(0, len(data)):
    print(data[tweet]["created_at"])
    print(data[tweet]["text"])
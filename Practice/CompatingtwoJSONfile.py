import json
path1 = "C:/Users/paneek/Documents/Automation/JsonFile/file_1.json"
path2 = "C:/Users/paneek/Documents/Automation/JsonFile/file_2.json"

with open(path1) as file1:
    content1 = json.load(file1)

with open(path2) as file2:
    content2 = json.load(file2)

print(content1==content2)

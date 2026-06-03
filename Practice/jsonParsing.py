import json
"""
courses = '{"array": [1,2,3],"boolean": true,"color": "gold","null": null ,"number": 123,"object": {"a": "b", "c": "d"},"string": "Hello World"}'
# loads method is used to parse a JSON string and convert it into a Python dictionary

dictionary = json.loads(courses)

print(type(dictionary))  # Output: <class 'dict'>
print(dictionary)  # Output: {'array': [1, 2, 3], 'boolean': True, 'color': 'gold', 'null': None, 'number': 123, 'object': {'a': 'b', 'c': 'd'}, 'string': 'Hello World'}

# Accessing values in the dictionary
print(dictionary["object"]['c'])
print(dictionary["array"][0])  # Output: 2

### **************  JSON File Parsing ************** ###
# Correct usage of json.load() to read a JSON file
path = "C:/Users/paneek/Documents/Automation/JsonFile/file.json"
with open (path, "r") as file:
    content = json.load(file)
# print(content)
print(content["courses"][1]["site_name"])
"""

##### ******** without using the indexing ************** #####
path = "C:/Users/paneek/Documents/Automation/JsonFile/file.json"
with open(path, "r") as file:
    content = json.load(file)  # Pass the file object directly to json.load()
    data = content["courses"]
    # print(type(data))  # Output: <class 'list'>
    for course in data:
        # print(course)
        if course["title"] == "Python":
            print(course["price"])
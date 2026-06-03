import requests
import json

url = "https://reqres.in//api/users?page=2"

headers = {"x-api-key": "reqres-free-v1"}

response = requests.get(url, headers=headers)
if response.status_code ==200:
    data =response.json()
    print("API Response:")
    print(json.dumps(data, indent=4))  # Pretty print the JSON response
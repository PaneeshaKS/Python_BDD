import requests
import json


# This script sends a GET request to the ReqRes API to fetch users from page 2
headers = {
    "x-api-key": "reqres-free-v1"
}

url = "https://reqres.in/api/users?page=2"
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.headers)
print(json.dumps(response.json(), indent=4))

# Post request to create a user

url = "https://reqres.in/api/users"
data = {
    "name": "John Doe",
    "job": "Software Engineer"
}
response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.headers)
print(json.dumps(response.json(), indent=4))

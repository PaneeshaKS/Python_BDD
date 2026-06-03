import requests
import json

url = "https://reqres.in/api/users/2"
headers = {"x-api-key": "reqres-free-v1"}
data = {
    "name": "morpheus",
    "job": "zion resident"
}

response = requests.put(url,json=data, headers=headers)
print("Response Status Code:", response.status_code)
print("Response JSON:", response.json())
assert response.status_code == 200
assert response.json()["name"] == "morpheus"
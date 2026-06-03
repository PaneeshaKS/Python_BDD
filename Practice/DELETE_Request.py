import requests
import json

url = "https://reqres.in/api/users/2"
headers = {"x-api-key": "reqres-free-v1"}

response = requests.delete(url, headers=headers)
print("Response Status Code:", response.status_code)
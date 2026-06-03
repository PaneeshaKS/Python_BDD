import requests
import json

url = "https://reqres.in//api/users?delay=3"
headers = {    "Content-Type": "application/json",
           "x-api-key": "reqres-free-v1"
}

response = requests.get(url, headers=headers, timeout=4)
print("Response Status Code:", response.status_code)
# print("Response Headers:", response.headers)
# print("Response Content:", response.text)
# If the response is in JSON format, you can parse it
print(json.dumps(response.json(), indent=4))
print("Response JSON:", response.status_code)
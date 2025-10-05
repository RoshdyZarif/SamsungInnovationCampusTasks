import requests

URL = "http://127.0.0.1:5000/temperature"

response = requests.get(URL)
print("GET Response:", response.json())


new_value = 30.2
response = requests.post(URL, json={"value": new_value})
print("POST Response:", response.json())


response = requests.get(URL)
print("GET Response:", response.json())

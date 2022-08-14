import requests


BASE_URL = "http://127.0.0.1:5000/"

response = requests.get(BASE_URL)
tasks = response.json()

print(tasks)

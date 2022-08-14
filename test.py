import json
import requests


BASE_URL = "http://127.0.0.1:5000/"

response = requests.get(BASE_URL)
tasks = response.json()

with open("tasks.json", "w") as f:
    json.dump(list(tasks), f, indent=2)

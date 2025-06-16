import requests

url = "https://github.com/nicoscAIdev"

req = requests.get(url)

print(req.status_code)
import requests

url = 'http://127.0.0.1:5000/predict'
data = {"text": "Breaking: New study proves COVID-19 vaccine saves lives"}

response = requests.post(url, json=data)
print(response.json())

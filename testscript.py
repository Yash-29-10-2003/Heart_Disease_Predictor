import requests
import json

url = 'http://127.0.0.1:5000/predict'  

input_data = {
    'age': 50,
    'sex': 1,
    'cp': 0,
    'trestbps': 120,
    'chol': 250,
    'fbs': 0,
    'restecg': 0,
    'thalach': 175,
    'exang': 0,
    'oldpeak': 1.2,
    'slope': 2,
    'ca': 0,
    'thal': 3
}

response = requests.post(url, json=input_data)

print(response.status_code)
print(response.json())
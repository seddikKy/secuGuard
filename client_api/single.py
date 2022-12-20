import requests

endpoint = "http://127.0.0.1:8000/product/5/" #"http://httpbin.org/anything" 
response = requests.get(endpoint)
#print(response.text)
print(response.json())
print(response.status_code)
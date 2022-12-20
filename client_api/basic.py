import requests

endpoint = "http://127.0.0.1:8000/product/" #"http://httpbin.org/anything" 
response = requests.post(endpoint, json={'name':'Pasteque','content':'Add from client_api','price':12.99})
#print(response.text)
print(response.json())
print(response.status_code)
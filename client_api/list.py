import requests

endpoint = "http://127.0.0.1:8000/api/employee/list-create/" #"http://httpbin.org/anything" 
header = {
    'Authorization' : 'Bearer 92325ff1b71a903243dd9b726f0237bd5561bbd4'
    # 'Authorization' : 'Token 746b9a51dff3d9f54a894fcb67ea3a8ff75a9dec'
}
response = requests.get(endpoint, headers=header, json={'name':'Orange 200','content':'','price':300})
#print(response.text)
print(response.json())
print(response.status_code)
import requests

endpoint = "http://127.0.0.1:8000/api/site/4/update" #"http://httpbin.org/anything" 
header = {
    'Authorization' : 'Bearer 92325ff1b71a903243dd9b726f0237bd5561bbd4'
}
response = requests.patch(endpoint, headers=header, json={'name':'Site_A'})
#print(response.text)
print(response.json())
print(response.status_code)
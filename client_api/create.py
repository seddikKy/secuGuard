import requests
from getpass import getpass
endpoint = "http://127.0.0.1:8080/auth" 
username = input("entrer votre nom d'utilisateur : \n")
password = getpass("Entrer votre password :  \n")
auth_response = requests.post(endpoint, json={'username':username,'password':password})

print(auth_response.json())
if auth_response.status_code == 200 :
    endpoint = "http://127.0.0.1:8080/create/" #"http://httpbin.org/anything" 
    header = {
        'Authorization' : 'Bearer 92325ff1b71a903243dd9b726f0237bd5561bbd4'
        # 'Authorization' : 'Token 746b9a51dff3d9f54a894fcb67ea3a8ff75a9dec'
    }

    response = requests.get(endpoint,headers=header)
    #print(response.text)
    print(response.json())
    #print(response.json())
    print(response.status_code)
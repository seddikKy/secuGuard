import requests

id = input('Entrée le id du produit à supprimer : ')
endpoint = f"http://127.0.0.1:8000/product/{id}/delete" #"http://httpbin.org/anything" 
response = requests.delete(endpoint)

print(response.status_code, response.status_code==204)
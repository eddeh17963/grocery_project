import requests
import base64
import json

CLIENT_ID = 'edderapp-ec15a8dde77ce54aa1b7248b6c5f2b381967857996314739994'
CLIENT_SECRET = 'x0M84ruSVYDLWXkvon2XnN8wk9_QiCGEdQJsSW3B'
AUTH_URL = 'https://api.kroger.com/v1/connect/oauth2/token'
encoded_client_token = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode('ascii')).decode('ascii')

def get_client_access_token(encoded_client_token):
    url = AUTH_URL
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {encoded_client_token}',
    }
    payload = {
        'grant_type':"client_credentials",
        'scope':['product.compact'],
    }
    response = requests.post(url, headers=headers, data=payload)
    return json.loads( response.text).get('access_token')

def 

access_token = get_client_access_token(encoded_client_token)

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}',
}

BASE_URL = 'https://api-ce.kroger.com/v1/'
urll = "https://api.kroger.com/v1/products?filter.term=chicken"

r = requests.get(urll, headers=headers)


print(r.json())


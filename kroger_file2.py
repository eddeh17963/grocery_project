
import requests
import base64
import json

# for certificate application
CLIENT_ID = 'edderapp-ec15a8dde77ce54aa1b7248b6c5f2b381967857996314739994'
CLIENT_SECRET = 'x0M84ruSVYDLWXkvon2XnN8wk9_QiCGEdQJsSW3B'
AUTH_URL = 'https://api.kroger.com/v1/connect/oauth2/token'

# CLIENT ID for Certificate application
# edderapp-ec15a8dde77ce54aa1b7248b6c5f2b38819516625572695243

# CLIENT SECRET for Certificate application
# RIViFVhzjWSzwW5YZj299oks-OJ9CeB0kfEL2icc

def get_access_token(url, client_id, client_secret):

    id_and_sec = CLIENT_ID + ":" + CLIENT_SECRET
    encoded = id_and_sec.encode("ascii") 
    encoded = base64.b64encode(encoded)
    encoded = encoded.decode("ascii") 
    #print(encoded)

    response = requests.post(url, {
    #'grant_type': 'client_credentials',
    #'client_id': client_id,
    #'client_secret': client_secret,
    "grant_type": "client_credentials",
    "User-Agent": "",
    "Authorization": f"Basic {encoded}",
    "Content-Type": "application/x-www-form-urlencoded"
    })

    return response.json()#['access_token']

def get_access_token2(url, client_id, client_secret):
    response = requests.post(
        url,
        data={"grant_type": "client_credentials",
              "scope": "product.compact"
        
        },
        auth=(client_id, client_secret),
    )
    return response.json()["access_token"]

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
    return json.loads(response.text).get('access_token')

access_token = get_client_access_token(encoded_client_token)
#access_token = get_access_token(AUTH_URL, CLIENT_ID, CLIENT_SECRET)
print(access_token)

#access_token = 'eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYXBpLmtyb2dlci5jb20vdjEvLndlbGwta25vd24vandrcy5qc29uIiwia2lkIjoiWjRGZDNtc2tJSDg4aXJ0N0xCNWM2Zz09IiwidHlwIjoiSldUIn0.eyJhdWQiOiJlZGRlcmFwcC1lYzE1YThkZGU3N2NlNTRhYTFiNzI0OGI2YzVmMmIzODE5Njc4NTc5OTYzMTQ3Mzk5OTQiLCJleHAiOjE3MTk0NDEwNTIsImlhdCI6MTcxOTQzOTI0NywiaXNzIjoiYXBpLmtyb2dlci5jb20iLCJzdWIiOiJhZGE2ZGZmNS02OTA1LTU3NjMtODRkYy1lYzYxN2Y5NWE3OTciLCJzY29wZSI6InByb2R1Y3QuY29tcGFjdCIsImF1dGhBdCI6MTcxOTQzOTI1MjYyNTcyNDI1MSwiYXpwIjoiZWRkZXJhcHAtZWMxNWE4ZGRlNzdjZTU0YWExYjcyNDhiNmM1ZjJiMzgxOTY3ODU3OTk2MzE0NzM5OTk0In0.OiEMfWtBLuEDyoe4hE2HuBh8fq6arn6Mb8ptXvBoKGrR5mHwReEIaiNSnMoX-0ZVQDN8rQ0tLRBKq-dQJdpGDB1TgQLiOoaLgtjiPf6FM5sn9dCjRZTke-fyfrPpjgPum0FYAptd0sNputhbAI2P3KUwJWS5mefieLSwuhZh_nP1n8zAwTGpQ3MGQYVNZ_9YPh_3b5n_ZSGpGO-J4dNP4VTd94oqnxrYxM9Oo-JKtBA28q4Xp08_gifQ9mgmmFuWraqGXKj8OuYmohdEk63d_RQkROhzGo-d5jgcsTS-Kvfqv7Ef98jWtxLXlbDjd-uadxGpwgGtY1ho4S0LvrKIAA'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}',
}


BASE_URL = 'https://api-ce.kroger.com/v1/'
urll = "https://api.kroger.com/v1/products?filter.term=chicken"
u = BASE_URL + 'products' + "?filter.term=fat%20free%20milk"
print(urll)
print(u)
#r = requests.get(BASE_URL + 'products' + "?filter.term=fat%20free%20milk", headers=headers)
r = requests.get(urll, headers=headers)


print(r.json())


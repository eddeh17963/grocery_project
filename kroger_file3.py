import requests
import base64
import json
import sqlalchemy as db
import pandas as pd
import pprint

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

def get_chicken_stats():
  access_token = get_client_access_token(encoded_client_token)
  headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}',
  }

  url = "https://api.kroger.com/v1/products?filter.term=chicken&filter.locationId=03400378"
  #url = 'https://api.kroger.com/v1/locations?filter.zipCode.near=77449&filter.radiusInMiles=5'

  return requests.get(url, headers=headers)

#print(json.dumps(get_chicken_stats().json(), indent=3))
copy = get_chicken_stats().json()['data'].copy()

ret = []
for i in range(len(copy)):
  cop = dict(copy[i])

  #print(cop)
  del cop['images']
  del cop['productPageURI']
  del cop['categories']
 
  cop['aisle decription'] = cop['aisleLocations'][0]['description']
  cop['aisle number'] = cop['aisleLocations'][0]['number']
  
  del cop['aisleLocations']
  cop["itemId"] = cop['items'][0]["itemId"]
  cop["priceRegular"] = cop['items'][0]["price"]['regular']
  cop["pricePromo"] = cop['items'][0]["price"]['promo']
  del cop['items']
  del cop['itemInformation']
  del cop['temperature']
  ret.append(cop)
  



#print(json.dumps(ret, indent=3))

chicken_items_db = pd.DataFrame.from_dict(ret)
engine = db.create_engine('sqlite:///chicken_items.db')
chicken_items_db.to_sql('chicken', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM chicken;")).fetchall()
   print(pd.DataFrame(query_result))







'''
This is an example illustrating ta simple request with client token authentication

For a guide how to obtain access and credentials go to : https://www.barentswatch.no/om/api-vilkar
The request demonstrated here is documented at this page: https://code.barentswatch.net/wiki/display/BWOPEN/FiskInfo

With a token and a valid permit this API have a response with fishing facilities including ship info
Without a token and valid permit the API have a respond with anonyms fishing facilities without ship info

 '''

import requests
import json
from pprint import pprint
import time
from credentials import config #Import config with username/password        config={'api_user': '', 'api_password': ''}

token ={}

def get_token():
      req = requests.post("https://www.barentswatch.no/api/token",
            data={
                  'grant_type': 'client_credentials',
                  'client_id': config['api_user'],
                  'client_secret': config['api_password']
            },
            params={},
            headers={'content-type': 'application/x-www-form-urlencoded'})
        
      token = req.json()
      #token = temp['access_token'].encode("ascii", "ignore")
      return token


def get_fishingfacilities(token):
  
  url = "https://www.barentswatch.no/api/v1/geodata/download/fishingfacility/?format=JSON"
  access_token = token['access_token'].encode("ascii", "ignore")
  headers ={
    'authorization': "Bearer " + access_token,
    'content-type': "application/json",
	}

  response = requests.get(url, headers=headers)
  if response.status_code == requests.codes.ok:
    return response.json()
  else:
    return "Error"


token = get_token();

fishingfacility = get_fishingfacilities(token)
timestr = time.strftime("%Y-%m-%d_%H%M%S")
with open('fishingfacility_'+timestr+'.geojson', 'w') as outfile:
    json.dump(fishingfacility, outfile)


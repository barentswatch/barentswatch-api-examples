import requests
import json
from pprint import pprint
import time
from credentials import config

token ={}

def get_token():
      req = requests.post("https://www.barentswatch.no/api/token",
            data={
                  'grant_type': 'password',
                  'username': config['api_user'],
                  'password': config['api_password']
            },
            params={},
            headers={'content-type': 'application/x-www-form-urlencoded'})
 
      return req.json()


def get_fishingfacilities(token):
	url = "https://www.barentswatch.no/api/v1/geodata/download/fishingfacility/?format=JSON"
	token2 = token['access_token'].encode("ascii", "ignore")

	headers ={
		'authorization': "Bearer " + token2,
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
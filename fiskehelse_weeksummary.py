import requests
import json
from pprint import pprint
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

def get_week_summary(token, year, week):
	url = "https://www.barentswatch.no/api/v1/geodata/fishhealth/locality/"+year+"/"+week
	token_bearer = token['access_token'].encode("ascii", "ignore")
	headers ={
		'authorization': "Bearer " + token_bearer,
        'content-type': "application/json",
	}

	response = requests.get(url, headers=headers)
	if response.status_code == requests.codes.ok:
		return response.json()
	else:
		return "Error"


token = get_token()

weeksummary= get_week_summary(token,"2017","45")
pprint(weeksummary)

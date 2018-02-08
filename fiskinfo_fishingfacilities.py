'''
This is an example illustrating ta simple request with token authentication

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
                  'grant_type': 'password',
                  'username': config['api_user'],
                  'password': config['api_password']
            },
            params={},
            headers={'content-type': 'application/x-www-form-urlencoded'})
 
      return req.json()


def get_fishingfacilities(token):
	"""
    Get fishing facilities with ship indentifiers

    Parameters
    ----------
    token : token json object

    Returns
    -------
    jsonobject
        json object with all current fising facilities with ship indentifiers

    """
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
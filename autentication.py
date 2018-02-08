#autentication
import requests
import json
from pprint import pprint
from credentials import config #Import config with username/password        config={'api_user': '',	'api_password': ''}

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

    if req.status_code == requests.codes.ok:
		print "status: "+ str(req.status_code)
		return req.json()
    else:
		print "status: "+ str(req.status_code)
		return "Error"

 			
      

token = get_token();

print "***********"
if token['access_token']:
  print "The complete token json object"

  pprint(token)
  print "***********"
  print "The token Attribute that must be used in any further requests"
  pprint(token['access_token'])
else:
  print "No token received"

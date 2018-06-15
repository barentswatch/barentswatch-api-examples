#autentication
import requests
import json
from pprint import pprint
from credentials import config #Import config with username/password        config={'api_user': '',	'api_password': ''}

token ={}


def get_client_token():

    req = requests.post("https://www.barentswatch.no/api/token",
            data={
                  'grant_type': 'client_credentials',
                  'client_id': config['api_user'],
                  'client_secret': config['api_password']
            },
            params={},
            headers={'content-type': 'application/x-www-form-urlencoded'})

    if req.status_code == requests.codes.ok:
		  print "status: "+ str(req.status_code)
		  return req.json()
    else:
      print "status: "+ str(req.status_code)
      print req.json()
      return "Error"

 			
      

token = get_client_token()
print token
print "***********"
if 'access_token' in token:
  print "The complete token json object"

  pprint(token)
  print "***********"
  print "The token Attribute that must be used in any further requests"
  pprint(token['access_token'])
else:
  print "No token received se error message above"

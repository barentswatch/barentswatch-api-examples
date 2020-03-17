import requests
from pprint import pprint
from authentication import get_token
from credentials import config

def make_sample_request(token):
  url = f"{config['api_base_url']}/v1/sample/auth"
  headers ={
    'authorization': 'Bearer ' + token['access_token'],
    'content-type': 'application/json',
  }

  response = requests.get(url, headers=headers)
  response.raise_for_status()
  return response.json()


if __name__== "__main__":
  token = get_token()
  response = make_sample_request(token)
  print('Request to the api was successful - authentication worked.')
  pprint(response)


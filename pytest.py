#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from credentials_thh import config


def get_token():
      req = requests.post("https://www.barentswatch.no/api/token",
            data={
                  'grant_type': 'password',
                  'username': config['api_user'],
                  'password': config['api_password']
            },
            params={},
            headers={'content-type': 'application/x-www-form-urlencoded'})
 
      print req.text

get_token();
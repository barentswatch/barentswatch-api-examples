# Barentswatch-api-examples

This is a set of python files that demonstrate the use of Barentswatch API.
The official API documentation is here: https://code.barentswatch.net/wiki/display/BWOPEN/API-Documentation

Python3 is required and the package requests needs to be installed:
``` bash
> pip install requests
```

Edit credentials.py and insert your client_id and client_secret.

Get token:
``` bash
> python authentication.py
```


Get token and verify that the token is valid for the api:
``` bash
> python test_token.py
```


Get token and make api-call:
``` bash
> python fiskehelse_weeksummary.py
```

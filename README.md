# Barentswatch-api-examples

This is a set of python files that demonstrate the use of Barentswatch API.
The official API documentation is her: https://code.barentswatch.net/wiki/display/BWOPEN/API-Documentation


The purpose of this project is to have some example files for support request for future users of the Barentswatch API.

file |purpose
------------- | -------------
Crendentials.py | config file to hold the credentials to authenticate  with
autentication.py | demonstrate how to get an authorization  token with user/password (user Authorization)
autentication_with_client_token.py| demonstrate how to get an authorization  token with client credentials (app Authorization)
fiskelse_weeksummary.py| Authentication with client token and then using the in a simple request with fiskehelse
fiskinfo_fishingfacilities| Using client Authentication and dumping all fishing facilities to a local geojsonfile. If the account does not have the right priviliges the data will be anonymized.

https://www.barentswatch.no/om/api-vilkar

# Error handling
Error code 400 and error messages:

"invalid_client" : Something wrong with you credentials (username/password)
Either wrong username/passord or you have not registered for an user account

Error code 400 and "'User not approved for requested grant type: password'"
You have a valid autentication but do not have the right permissions.
You could try to use grant type "client_credentials" or contact post@barentswatch.no
Error code 400 and "User not approved for requested grant type: client_credentials"

You have a valid autentication but do not have the right permissions.
You could try to use grant type "password" or contact barentswatch.no

Error code 500
Something wrong with the server






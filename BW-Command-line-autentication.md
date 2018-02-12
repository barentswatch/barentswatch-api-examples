#Barentswatch command-line examples

##Curl
Autenticate and fetch data with curl commands

### First get your token.
This command autenticate and save the repons in a txt file

```bash
curl -k -X POST -d 'grant_type=password&username=trond.hanssen@bouvet.no&' https://www.barentswatch.no/api/token -o token.txt
```
Content of token.txt:

```json
{"access_token":"dnRB1k9IcFL-f4zgfh-XnDMsknVxsVlfG6j21PJWj27HDxIdJvdX3Yzwig3ba5aGB1jdmn6gYy4TLbBufDh12qOjhLQml2KyxTcsFBu54pbKP0U7glBSDYPbj2HSOt9Z5wNpMQrrQtkWy6lL2cHVxb4DbMb4MLEDEm-hp8BCPvNjEGL-PEmcdjbcw13V1R49VgVMYVBOBWcO47YbegPsqTOGALljrKHrp9kcjyAfzDedrQ27cSym9Rf_i9vDvgYG-EcvfqCaWRY0Nmc22Qxx5QROwBI-E8SCoxcpJ7QpbyDyIEQjyEZpRenvKCIqHHY88Jd1yYCp6SIutziPM57aNsD6itBErumOjUTDClA6WJY_xPhLZDQJvXLMGdDyzN4LCb8jRScR3MWRP-pYD1ESkA","token_type":"bearer","expires_in":43199}
```


### then fetch data with autentication token
When you have your token you can use that to fetch data as autenticated user

```bash
curl -k -H 'Authorization: Bearer $access_token' https://www.barentswatch.no/api/v1/geodata/download/fishingfacility/?format=JSON -o result2.json

```

Replace $access_token with the value from json atribute withe same name from the first respons


It is reqomended to autenticate and fetch data programatically.
OAuth autentication is widely used and 
Here is a list of  client libraries in many languages.
https://oauth.net/code/
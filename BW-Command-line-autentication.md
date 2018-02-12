Barentswatch comand-line examples

Curl

First get your token.
This command autenticate and save the repons in a txt file
curl -k -X POST -d 'grant_type=password&username=trond.hanssen@bouvet.no&' https://www.barentswatch.no/api/token -o token.txt

Content of token.txt:

{"access_token":"dnRB1k9IcFL-f4zgfh-XnDMsknVxsVlfG6j21PJWj27HDxIdJvdX3Yzwig3ba5aGB1jdmn6gYy4TLbBufDh12qOjhLQml2KyxTcsFBu54pbKP0U7glBSDYPbj2HSOt9Z5wNpMQrrQtkWy6lL2cHVxb4DbMb4MLEDEm-hp8BCPvNjEGL-PEmcdjbcw13V1R49VgVMYVBOBWcO47YbegPsqTOGALljrKHrp9kcjyAfzDedrQ27cSym9Rf_i9vDvgYG-EcvfqCaWRY0Nmc22Qxx5QROwBI-E8SCoxcpJ7QpbyDyIEQjyEZpRenvKCIqHHY88Jd1yYCp6SIutziPM57aNsD6itBErumOjUTDClA6WJY_xPhLZDQJvXLMGdDyzN4LCb8jRScR3MWRP-pYD1ESkA","token_type":"bearer","expires_in":43199}




curl -k -X POST -b token.txt https://www.barentswatch.no/api/geodata/download/fishingfacility/?format=JSON -o result.json



It is reqomended to autenticate and fetch data programatically.
OAuth autentication is widely used and 
Here is a list of  client libraries in many languages.
https://oauth.net/code/
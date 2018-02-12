#!/bin/bash
#bw_autentication_curl_bash_script
#This is an example of autentication and fetching data as autenticated user.
#The autenticated user has be autorized first.

# this script is not finish yet do not use before it is finish and tested

$tokenPath="https://www.barentswatch.no/api/token"
$dataPath="https://www.barentswatch.no/api/v1/geodata/download/fishingfacility/?format=JSON"


getLogin() {
    read -p "Please enter username: " username
    read -p "Please enter reponame: " repo
    reponame=${username}/${repo}
    if [ -n "$username"  ]; then
        read -s -p "password: " password
        echo
    fi
}

getBearerToken() {
    local HEADERS
    local RESPONSE

    if [ -n "$username"  ]; then
        HEADERS="Authorization: Basic $(echo -n "${username}:${password}" | base64)"
    fi
    echo [+] Logging in
    curl -s -H "$HEADERS" "$tokenPath" | jq '.token' -r > token.txt
    echo [+] Got Bearer token
}

downloadData() {
    #local reponame=$1
    #local blobDigest=$2
    local token=$(getToken)

    echo "Downloading Data"
    time curl -L --progress-bar -H "Authorization: Bearer $(cat token.txt)" "$dataPath" > download.json
}

getLogin
#uploadBlob $reponame
getBearerToken

for i in {1..10}; do
    downloadData 
done
#!/bin/bash
#bw_autentication_curl_bash_script
#This is an example of autentication and fetching data as autenticated user.
#The autenticated user has be autorized first.

# this script is not finish yet do not use before it is finish and tested

$tokenPath="https://www.barentswatch.no/api/token"
$dataPath="https://www.barentswatch.no/api/v1/geodata/download/fishingfacility/?format=JSON"


getLogin() {
    read -p "Please enter username (or empty for anonymous): " username
    if [ -n "$username" ]; then
        read -s -p "password: " password
        echo
    fi
}

getToken() {
    #local reponame=$1
    #local actions=$2
    local headers
    local response

    if [ -n "$username" ]; then
        headers="Authorization: Basic $(echo -n "${username}:${password}" | base64)"
    fi

    response=$(curl -s -H "$headers" "$tokenPath")

    echo $response | jq '.token' | xargs echo
}

downloadData() {
    #local reponame=$1
    #local blobDigest=$2
    local token=$(getToken)

    echo "Downloading Data"
    time curl -L --progress-bar -H "Authorization: Bearer $token" "$dataPath" > download.json
}

#getLogin
#uploadBlob $reponame

for i in {1..10}; do
    downloadData 
done
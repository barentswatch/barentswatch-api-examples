# Script that downaload and save akvakulturregisteret
import requests
import json
from pprint import pprint
import time
from credentials_thh import config

token ={}
localities=[]
akvareg=[]
orglist={}

#autenticate and get a token
def get_token():
      req = requests.post("https://www.barentswatch.no/api/token",
            data={
                  'grant_type': 'client_credentials',
                  'client_id': config['api_user'],
                  'client_secret': config['api_password']
            },
            params={},
            headers={'content-type': 'application/x-www-form-urlencoded'})
 
      return req.json()

def bw_request(url,token):
	token_bearer = token['access_token'].encode("ascii", "ignore")
	headers ={
		'authorization': "Bearer " + token_bearer,
        'content-type': "application/json",
	}

	response = requests.get(url, headers=headers)
	if response.status_code == requests.codes.ok:
		return response.json()
	else:
		return "Error"


#Get all localities
def get_localities():
	url = "https://www.barentswatch.no/api/v1/geodata/fishhealth/localities"
	#return (bw_request(url,token))
	bw_json=bw_request(url,token)
	#print bw_json
	#test = json.load(bw_json)
	#mylist = bw_json['localityNo']
	#print test
	return (bw_json)




def get_akvakulturregisteret(localities):
	base_url="https://www.barentswatch.no/api/v1/geodata/fishhealth/locality/"
	week=str("50")
	year=str("2017")
	aquareg =[]
	total= len(localities)
	print "Number of localities is: "+str(total)
	cnt=0
	for locality in localities:
		#if cnt< 20:
		cnt+=1
		print "fetching "+str(cnt)+" of "+str(total)+" lok: "+str(locality['localityNo'])
		url = base_url+str(locality['localityNo'])+"/"+year+"/"+week
		data = bw_request(url,token)
		if data['localityIsInAquaCultureRegister']==True and data['aquaCultureRegister'] is not None:
			organizations=data['aquaCultureRegister']['organizations']
			for org in organizations:
				element = org.pop('localities')
				orglist[org['organizationNo']]=org
		else:
			print "No org found for: "+str(locality['localityNo'])
	#return aquareg

def write2file(listDict):
	timestr = time.strftime("%Y-%m-%d_%H%M")
	with open('aquareg_'+timestr+'.json', 'w') as outfile:  
		json.dump(listDict, outfile)

start = time.time()
token = get_token();
localities = get_localities()
get_akvakulturregisteret(localities)
write2file(orglist)
end = time.time()
exec_time = end-start
cnt_org= len(orglist)
print "Finish: This script took "+str(exec_time)+" to run"
print "added "+ str(cnt_org)+" organizations to file "

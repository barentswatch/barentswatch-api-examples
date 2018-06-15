# Script that downaload and save akvakulturregisteret
import requests
import json
from pprint import pprint
import time
from credentials_thh import config

# Config variables
conf_remove_other_localities= True # remove other lovalitites own by companies owning the fetched localie
conf_akvareg = True
conf_complete=True
outputPath= "output/"

#Global variables
token ={}
datasett=[]
localities=[]
akvareg=[]
localities_by_week=[]


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
	#print token
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
def get_localities(token):
	#This API responds with a list of all localities ever been registered in the akvakulturregister
	url = "https://www.barentswatch.no/api/v1/geodata/fishhealth/localities"
	bw_json=bw_request(url,token)
	
	return (bw_json)

def fetch_localities(token,localities,year,week):
	base_url="https://www.barentswatch.no/api/v1/geodata/fishhealth/locality/"
	total= len(localities)
	print "Number of localities is: "+str(total)

	cnt=0
	for locality in localities:
		cnt+=1
		#temp={}
		print "fetching "+str(cnt)+" of "+str(total)+" lok: "+str(locality['localityNo'])
		url = base_url+str(locality['localityNo'])+"/"+year+"/"+week
		data = bw_request(url,token)
		
		localityWeek = data['localityWeek']
		localityWeek['localityName'] = data['localityName']
		localityWeek['IsInAquaCultureRegister'] = data['localityIsInAquaCultureRegister']
		if data['productionArea']:
			localityWeek['productionArea']= data['productionArea']['id']
		localityWeek['pdZoneId'] = data['pdZoneId']
		localities_by_week.append(localityWeek)
		if conf_akvareg:
			temp=parse_akvareg(data)
			if temp is not None:
				akvareg.append(temp)

		if conf_complete:
			datasett.append(data)




def parse_akvareg(data):
	#aquareg =[]
	#This function loop thru all localities and fetch data from the akvakulturregisteret for the spesific week
	
	if data['aquaCultureRegister']:
		print "ok"
		loc=data['aquaCultureRegister']
		if conf_remove_other_localities:
			for org in loc['organizations']:
				del org['localities']
			
	else:
		loc=None
		print "not in akvakulturregisteret"
	return loc 



def listDict2json(listDict,filename):
	with open(outputPath+filename, 'w') as outfile:  
		json.dump(listDict, outfile)
	#with open('aquareg_csv'+timestr+'.json', 'w') as outfile:  
		#json.dump(listDict, outfile)
	#return filename

def start_import():
	start = time.time()
	token = get_token()
	#print token
	localities = get_localities(token)
	current_year = time.strftime("%Y")
	current_week = time.strftime("%W")
	fetch_localities(token,localities,current_year,current_week)
	#aquareg = get_akvakulturregisteret(token,localities,current_year,current_week)
	timestr = time.strftime("%Y-%W_%m-%d_%H%M")
	filename = 'aquareg_json'+timestr+'.json'
	listDict2json(localities,'localities_json'+timestr+'.json')
	listDict2json(akvareg,'akvareg'+timestr+'.json')
	listDict2json(datasett,'datasett_json'+timestr+'.json')


	end = time.time()
	exec_time =  time.strftime("%H:%M:%S", time.gmtime(end-start))
	print "Finish: This script took "+str(exec_time)+" to run"
	return filename

start_import()
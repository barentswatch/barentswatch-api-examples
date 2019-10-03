#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
from pprint import pprint
import time
from credentials_thh import config #Import config with username/password        config={'api_user': '', 'api_password': ''}
from fiskinfo_fishingfacilities import get_fishingfacilities
#from autentication_with_client_token import
token ={}

def get_client_token():
    req = requests.post("https://www.barentswatch.no/api/token",
            data={
                  'grant_type': 'password',
                  'username': config['api_user'],
                  'password': config['api_password']
            },
            params={},
            headers={'content-type': 'application/x-www-form-urlencoded'})

    if req.status_code == requests.codes.ok:
		    print "Autentication, status: "+ str(req.status_code)
		    return req.json()
    else:
      print "Autentication, status: "+ str(req.status_code)
      print req.json()
      return "Error"


def get_shipinfo(mmsi):
	time.sleep(2)
	mmsi2=str(mmsi)
	url="https://www.barentswatch.no/api/v1/geodata/vessel/"+mmsi2
	token2 = token['access_token'].encode("ascii", "ignore")

	headers ={
		'authorization': "Bearer " + token2,
        'content-type': "application/json",
	}

	response = requests.get(url, headers=headers)
	if response.status_code == requests.codes.ok:
		return response.json()
	else:
		return "Error"

def make_kvs_shiplist(facilities):
	print "Extracting ships from facilities"
	shiplist={}
	for element in facilities['features']:
		temp=element['properties']
		if temp['mmsi'] is not None:
			mmsi=temp['mmsi']
			if mmsi not in shiplist:
				shiplist[mmsi]=temp
			else:
				olddate=shiplist[mmsi]['setupdatetime']
				newdate=temp['setupdatetime']
				if newdate > olddate:
					shiplist[mmsi]=temp
	print "retrived "+ str(len(shiplist))+ " from " +str(len(fishingfacility['features']))+" facilities"
	return shiplist	

def parse_ships(kvsships):
	print "merging KVS shipinfo with BW shipinfo"
	#shiplist=[]
	#pprint(kvsships)
	kvscnt=len(kvsships)
	cnt=0
	bwcnt=0

	for key, element in kvsships.iteritems():
		cnt+=1
		#print str(cnt)+" of "+str(kvscnt)+" : "+ str(element['mmsi']) + " - "+ element['vesselname']
		#print element['mmsi']

		
		if cnt< 8000:
			data=get_shipinfo(int(element['mmsi']))
			if "mmsi" in data:
				print str(cnt)+" of "+str(kvscnt)+" : "+ str(element['mmsi']) #+ " - "+ element['vesselname']
				bwcnt+=1
				kvsships[key]['bw_shipRegister']=data['shipRegister']
				kvsships[key]['bw_shipRegisterName']=data['shipRegisterName']
				kvsships[key]['bw_aisName']=data['aisName']
				kvsships[key]['bw_ais']=data['ais']
				kvsships[key]['bw-name']=data['name']
				kvsships[key]['bw-imo']=data['imo']
				kvsships[key]['bw-ircs']=data['ircs']
				kvsships[key]['inBW']=True
				if kvsships[key]['vesselname'] is not None and data['name'] is not None:
					kvsships[key]['samename']=NameCompare(kvsships[key]['vesselname'],data['name'])
			else:
				print str(cnt)+" of "+str(kvscnt)+" : no mmsi"
				kvsships[key]['bw_shipRegister']=None
				kvsships[key]['bw_shipRegisterName']=None
				kvsships[key]['bw_aisName']=None
				kvsships[key]['bw_ais']=None
				kvsships[key]['bw-name']=None
				kvsships[key]['inBW']=False
				kvsships[key]['bw-imo']=None
				kvsships[key]['bw-ircs']=None
				kvsships[key]['samename']=None


	print str(bwcnt)+ " ships merged/found out of "+ str(len(kvsships))		
	return kvsships

def NameCompare(kvsname,bwname):
	bwname=bwname.replace("Æ".decode('utf-8'),'AE')
	bwname=bwname.replace("Ø".decode('utf-8'),'OE')
	bwname=bwname.replace("Å".decode('utf-8'),'AA')
	if bwname==kvsname:
		return True
	else:
		return False

def json2file(ships):
	#jsondata=s.json()
	timestr = time.strftime("%Y-%m-%d_%H%M%S")
	with open('KVS_BW_shiplist'+timestr+'.geojson', 'w') as outfile:
		json.dump(ships, outfile)

		
		




token = get_client_token();
#print token
print "Pulling fishingfacility"
fishingfacility = get_fishingfacilities(token)

shiplist= make_kvs_shiplist(fishingfacility)

newshiplist=parse_ships(shiplist)
json2file(newshiplist)


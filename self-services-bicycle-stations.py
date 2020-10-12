import requests
import json
from pymongo import MongoClient

def get_vlille():
    url="https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=3000&face=libelle&facet=nom&facet=commune&face=etat&facet=type&facet=etatconnexion"
    response=requests.request("GET",url)
    response_json=json.loads(response.text.encode("utf8"))
    return response_json.get("records",[])


def getSelfServicesBicycleStations(data):
    records=[]
    for elem in data:
        geolocations=elem['fields']['geo']
        size=elem['fields']['nbvelosdispo']
        name=elem['fields']['nom']
        tpe=elem['fields']['type']
        available=elem['fields']['etat']
        records.append({"recordid":elem['recordid'],"geolocations":geolocations,"size":size,"name":name,"tpe":tpe,"available":available}) 
    return records

data=get_vlille()
records=getSelfServicesBicycleStations(data)

def putIntoDatabase(db,data):
    posts=db.posts
    post_id=posts.insert_one(data).inserted_id

client=MongoClient('localhost',27017)
client=MongoClient()
db=client.database

for elem in records:
    putIntoDatabase(db,elem)

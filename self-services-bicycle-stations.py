import requests
import json

def get_vlille():
    url="https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=3000&face=libelle&facet=nom&facet=commune&face=etat&facet=type&facet=etatconnexion"
    response=requests.request("GET",url)
    response_json=json.loads(response.text.encode("utf8"))
    return response_json.get("records",[])

data=get_vlille()
print(len(data))
for elem in data :
    print("Record ID : {} -> {}".format(elem['recordid'],elem['fields']))

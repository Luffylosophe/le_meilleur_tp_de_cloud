import requests
import json
from pprint import pprint
from pymongo import MongoClient


def get_geopositions_near_coord(cln,coord):
    
    cln.create_index([("geometry","2dsphere")]) 
    near_velo=cln.find({
        "geometry":{
                "$near" :{
                    "$geometry":{
                        "type":"Point",
                        "coordinates":coord
                    },
                    "$maxDistance":1000,
                    "$minDistance":0
                } 
        }})
    return near_velo

def print_velo_info(velo_list):
    for v in velo_list:
        print("Name : {} | Location : {}".format(v["name"],v["geometry"]["coordinates"]))
atlas = MongoClient("mongodb+srv://azerty1234:azerty1234@cluster0.7icpc.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = atlas.bicycle
bdd = db.vlille
coord2=[3.05849,50.6322]
positions = get_geopositions_near_coord(bdd,coord2)
print_velo_info(positions)
#positions = get_geopositions_near(vlilles,"bicycle")


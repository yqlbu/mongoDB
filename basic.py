import pymongo
import uuid
import time
import socket
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId


def get_ip():
    hostname = socket.gethostname()    
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IPAddr=s.getsockname()[0]
    s.close()
    return (hostname, IPAddr)

# ------------ Config connection ----------------#

CLUSTER_URL='url'
# Connection
cluster = MongoClient(CLUSTER_URL)

# Cluster 
db=cluster['jetson']

# Collection (DB Instance)
collection= db['instance-01']

# ------------ Define data format----------------#

# Data
post1={
    "time":datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    "client":get_ip()[0],
    "client_ip":get_ip()[1],
    "score":10
}

post2={
    "time":datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    "client":get_ip()[0],
    "client_ip":get_ip()[1],
    "score":100
}

# ------------ Insert data to db ----------------#

# Insert a post (entry)
collection.insert_one((post1))

# Insert multiple posts (entries)
collection.insert_many((post1,post2))

# ------------ Delete data ----------------#

result = collection.delete_many({}) # Delete all data
result = collection.delete_one({"_id":ObjectId('id')})

# ------------ Update data ---------------- #

# use the $set operator to update data for a specific post(entry)
results = collection.update_one({"_id":ObjectId('id')},{"$set":{'score':999}})

# ------------ Find multile data ---------------- #

# Find all posts (entries)
results=collection.find({}) 
for query in results:
    print(query)
    print(query['_id'])

# Find posts that satisfy certain creteria
results=collection.find({"client":'jetson-xavier'}) # name is the key,  kev is the value
for result in results:
    print(result) # print all posts(entries)
    print(result['_id']) # print all values associated with that key


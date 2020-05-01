import pymongo
import uuid
import time
import socket
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId

import sys
sys.path.append('./sensors')
from cpu import get_cpus
from disks import get_disks
from memory import get_memory
from fan import get_fans
from net import get_networks
from temperatures import get_temperatures
from internet_speed import get_internet_speed

class db:
    def __init__(self, CLUSTER_URL,CLUSTER_NAME,COLLECTION_NAME):
        url=CLUSTER_URL
        cluster_name=CLUSTER_NAME
        collection_name=COLLECTION_NAME
        # Connection
        self.cluster = MongoClient(url)
        # Cluster 
        self.db=self.cluster[cluster_name]
        # Collection (DB Instance)
        self.collection=self.db[collection_name]
    def get_ip(self):
        hostname = socket.gethostname()    
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        IPAddr=s.getsockname()[0]
        s.close()
        return (hostname, IPAddr)
    def show_all(self):
        # Display all data in the database
        query_dict={
            'total_post':0,
            'content':[]
        }
        results=self.collection.find({})
        for query in results:
            query_dict['total_post']+=1
            query_dict['content'].append(query)
        if query_dict['total_post']==0:
            print('No data find in database.')
        else:
            print("total number of posts: {}".format(query_dict['total_post']))
            print("database content: ")
            for x in query_dict['content']:
                print(x)
        # return query_dict
    def get_data_by_id(self,id):
        # Find a single post by its id
        results = self.collection.find({"_id":ObjectId(id)}) # name is the key,  kev is the value
        for result in results:
            return result # print all posts(entries)
    def get_data_by_field(self,field,value):
        # Find posts that satisfy certain creteria
        results=self.collection.find({field:value}) # name is the key,  kev is the value
        for result in results:
            return result # print all posts(entries)
    def remove_all(self):
        # Remove all data
        self.collection.delete_many({})
    def add_data(self,post):
        # Insert a post (entry)
        self.collection.insert_one(post)
    def remove_data(self,id):
        # Find a post (entry) based on its Id, then remove it from db
        self.collection.delete_one({"_id":ObjectId(id)})
    def update_data(self,id,field,value):
        # Find a post based on its Id, then update a value associated with its field
        # use the $set operator to update data for a specific post(entry)
        self.collection.update_one({"_id":ObjectId(id)},{"$set":{field:value}})
    def get_sensors_data(self):
        self.sensors_data={
            "cpu_load":str(get_cpus()[0]['data'])+'%',
            "temperature":get_temperatures()[0]['data']['Current'],
            "network_speed":get_networks()[0]['data'],
            "memory_space":{
                'Usage':str(get_memory()[1]['data'])+'%',
                'Total':str(get_memory()[0]['data']['Total']/1000)+'GB',
                'Used':str(get_memory()[0]['data']['Used']/1000)+'GB',
                'Available':str(get_memory()[0]['data']['Available']/1000)+'GB',
            },
            "swap_space":{
                'Usage':str(get_memory()[3]['data'])+'%',
                'Total':str(get_memory()[2]['data']['Total']/1000)+'GB',
                'Used':str(get_memory()[2]['data']['Used']/1000)+'GB',
                'Free':str(get_memory()[2]['data']['Free']/1000)+'GB'
            },
            "disk_usage":get_disks()
        }
        return self.sensors_data
    def help(self):
        print("*** Available functions are listed below:")
        array=[
            '(1) get_ip() \n'+
            '    --usage: Return Username and ipAddress of the device\n'+
            '    --params: none',
            '(2) show_all() \n'+
            '    --usage: Display all data in the database\n'+
            '    --params: none',
            '(3) get_data_by_id() \n'
            '    --usage: Return a single post by its id\n'+
            '    --params: id',
            '(4) get_data_by_field()\n'+
            '    --usage: Return a single post that satisfied certain criteria\n'+
            '    --params: field,value',
            '(5) add_data()\n'+ 
            '    --usage: Insert a post (entry) into db\n'+ 
            '    --params: post',
            '(6) remove_all()\n'+
            '    --usage: Remove all data from db\n'+ 
            '    --params: none',
            '(7) remove_data()\n'+ 
            '    --usage: Find a post (entry) based on its Id, then remove it from db\n'+ 
            '    --params: id',
            '(8) update_data()\n'+
            '    --usage: Find a post based on its Id, then update a value associated with its field\n'+ 
            '    --params: field,value'
            '(9) get_sensors_data()\n'+
            '    --usage: Return all sensors data from the local device\n'+
            '    --params: none'
        ]
        for x in array:
            print(x)
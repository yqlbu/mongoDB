# Jetson-mongoDB-Atlas

MongoDB Atlas is a fully-managed cloud database developed by the same people that build MongoDB. Atlas handles all the complexity of deploying, managing, and healing your deployments on the cloud service provider of your choice (AWS, Azure, and GCP). You may use this service totally **FOR FREE**.

**Notes:** This software is written in Python. You may use this repo as a tool to constantly post data (ie: sensors data) from your devices to your database hosted by MongoDB Atlas. The demo below is done with a Jetson AGX Xavier DevKit. Other edge devices such as Raspberry Pi and Jetson Nano, or a normal Linux Desktop should also work.

Official Website: https://docs.atlas.mongodb.com/ \
Blog Post: https://hikariai.net

## Demo

![](./demo_screenshots/001.png)
![](./demo_screenshots/002.png)

## Setup 

### Create a MongoDB Atlas Account

### Create a cluster

### Create a collection

## How To Use

### Clone the Repo

### Install Software Dependencies

Please make sure you are using Python >=3.6
```
pip install pymongo pymongo[srv]
pip install psutil
pip install speedtest-cli
```

### Run

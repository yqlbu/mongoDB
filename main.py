from db_module import db
import time
from datetime import datetime
import threading

URL = 'mongodb+srv://kev:439911@cluster0-fuzdr.gcp.mongodb.net/test?retryWrites=true&w=majority'
DATABASE_NAME ='jetson'
COLLECTION_NAME = 'instance-01'
SENT_INTERVAL = 60 # Sent data interval in second

db = db(URL,DATABASE_NAME,COLLECTION_NAME)

def main():
    # threading.Timer(SENT_INTERVAL, main).start() #  <-- comment out this line and the main func will be looped every 60s by default
    post={
        "time":datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "client":db.get_ip()[0],
        "client_ip":db.get_ip()[1],
        "sensors_data":db.get_sensors_data()
    }
    
    # Help
    # db.help()

    # Send data
    # db.add_data(post)

    # Remove all adata
    # db.remove_all()

    # Show all data
    db.show_all()

if __name__ == '__main__':
    main()
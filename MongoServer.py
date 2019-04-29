import datetime
from pymongo import MongoClient



def connectToMongo():
    client = MongoClient('localhost', 27017)
    connection = client["ANPR"]["PlateData"]
    return connection

def insert(connection,text):
    post = {}
    post['Plate Number'] = text
    post['Date'] = str(datetime.datetime.now().date())
    post['Time'] = str(datetime.datetime.now().time())
    print(datetime.datetime.now().time())
    connection.insert(post)




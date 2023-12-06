import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
my_database = client["currento"]
collection = my_database['currency_evo']

def insert_data(data):
    if data['success']==True:
        collection.insert_one(data)
        return {'success':True}
    else:
        return data

def insert_many(data):
    collection.insert_many(data)


def daily_average():
    pipeline = [
    {'$group': {'_id': '$date','MAD':{'$avg':'$rates.MAD'},'USD':{'$avg':'$rates.USD'}}},{'$sort':{'_id':-1}},{'$limit':7}
]
    result = list(collection.aggregate(pipeline))
    return result

def last_day_data():
    result = list(collection.find({},{'_id':0,'success':0,'base':0},sort=[('timestamp',1)],limit=24))

    for obj in result:
        timestamp = obj['timestamp']
        date_time = datetime.fromtimestamp(timestamp).strftime('%H:%M')
        obj['timestamp'] = date_time
    return result
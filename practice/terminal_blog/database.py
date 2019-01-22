import pymongo


class Database(object):
    url = "mongodb://127.0.0.1:27017"
    DATABASE = None


    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.urlurl)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection,data):
        Database.DATABASE[collection.insert(data)]

    @staticmethod
    def find(collection, query):
        Database.DATABASE[collection.find_one(query)
    @staticmethod
    def find(collection, query):
        Database.DATABASE[collection.find_one(query)


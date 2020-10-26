from pymongo import MongoClient
from bson.json_util import dumps

uri = 'mongodb://localhost:27017'

client = MongoClient(uri, connectTimeoutMS=2000, retryWrites=True)


def basic_usage():
    print(client.stats)
    print(client.list_database_names())
    print(client['sample_mflix'].list_collection_names())
    print(client['sample_mflix']['movies'].count_documents({}))

def find_usage():
    movies = client['sample_mflix']['movies']

    print(movies.find_one())        # Returns the first document
    # Queries or filters are turned into bson format by pymongo before sending as query
    print(movies.find_one({"cast": "Salma Hayek"}))     # Returns the first document with filter
    # Use of projections below on title and _id
    salma_hayek = movies.find({"cast": "Salma Hayek"}, {"title" : 1, "_id" : 0})     # Returns a cursor instead of docs
    print(movies.find({"cast": "Salma Hayek"}).count())     # Returns the count with filter
    print(dumps(salma_hayek, indent=2))

    print(dumps(movies.find({ "countries" : {"$in": ["USA"]}}, {"title"}).limit(1)))


if __name__ == "__main__":
    # basic_usage()
    # find_usage()
import time
import pymongo
from pymongo import MongoClient



def AccessTimeOutCheck(expiretime, token):
    if(expiretime > time.time()):
        return True
    else:
        try:
            client = MongoClient('mongodb+srv://Vishwas:Vishwasgowda@django.zyn54ai.mongodb.net/?retryWrites=true&w=majority')
            db = client['djangoproject']
            collection = db['login']
            delete_result = collection.delete_one({"token": token})
            client.close()
            if delete_result.deleted_count == 1:
                print(f"Document with token '{token}' deleted successfully.")
            else:
                print(f"No document found with token '{token}'.")
        except pymongo.errors.PyMongoError as e:
            print(f"Error deleting document: {e}")
        return False


# token = "eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJlbWFpbCI6ICJ2aXNod2FzLmVyMTQ1NjJAZ21haWwuY29tIiwgInN1YiI6ICJUT0tFTiIsICJhY2NfdGltZSI6IDE3MTc2NTcyNjAsICJleHBfdGltZSI6IDE3MTg5NTMyNjB9._1_Ode0qJWHEMxxmFtLVAJ8fT9qSgTilC89nrUu2Lws="
# print(AccessTimeOutCheck(1717656413, token))
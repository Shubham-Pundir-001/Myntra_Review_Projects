import pandas as pd 
from database_connect import mongo_operation as mong 
import os,sys
from src.constants import *
from src.exception import CustomException
class MongoIo:
    mongo_ins=None

    def __init__(self):
        if MongoIo.mongo_ins is None:
            mongo_db_url="mongodb+srv://shubham:9012885070@cluster0.jcwkp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            if mongo_db_url is None:
                raise Exception(f" enviornment key:{MOGODB_URL_KEY} is not set")
            MongoIo.mongo_ins=mong(client_url=mongo_db_url,
                                   database_name=MOGODB_DATABASE_NAME)
            self.mongo_ins=MongoIo.mongo_ins

    def store_reviews(self,proudct_name:str, reviews:pd.DataFrame):
        try:
            collection_name=proudct_name.replace(" ","_")
            self.mongo_ins.bulk_insert(reviews,collection_name)
        except Exception as e:
            raise CustomException(e,sys)
        
    def get_reviews(self,product_name:str):
        try:
            data=self.mongo_ins.find(collection_name=product_name.replace(" ","-"))
            return data
        except Exception as e:
            raise CustomException(e,sys)

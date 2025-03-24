from src.cloud_io import MongoIo
from src.constants import MOGODB_DATABASE_NAME
from src.exception import CustomException
import sys ,os
 

def fetch_product_name_cloud():
    try:
        mongo=MongoIo()
        collection_names=mongo.mong_ins_.mongo_operation_connect_database.list_collection_names()
        return [collection_name.replace('_',' ')
            for collection_name in collection_names]
    except Exception as e:
        raise CustomException(e,sys)
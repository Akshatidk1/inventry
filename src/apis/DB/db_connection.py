from src.apis.DB.MySqlWrapper import *
from src.apis.DB.database import *

def db_connect():
    db = MySQLWrapper(host='127.0.0.1', user='root', password="Shared123", database='demo')
    return db

# db_connect()

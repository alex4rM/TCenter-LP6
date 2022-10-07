from pymongo import MongoClient
import pymongo

MONGO_URI = 'mongodb://localhost'
def dbConection():
    try:
        client = MongoClient(MONGO_URI,serverSelectionTimeoutMS=1000)
        db = client['pruebaMongo']
        client.server_info()
        print('Exito!!')
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print('Tiempo exedido '+errorTiempo)  
    except pymongo.errors.ConnectionFailure as errorConexion:
        print('No conectado con mongodb '+errorConexion)
    return db
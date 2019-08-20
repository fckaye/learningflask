from pymongo import MongoClient

MONGO_URI = ""

def db_connect(MONGO_URI, db_name, col_name):
    client = MongoClient(MONGO_URI)
    database = client[db_name]
    collection = database[col_name]
    return collection

def db_insert_user(collection, user):
    return collection.insert_one(user)

def db_find_all(collection, query={}):
    """Function to fetch content in collection"""
    return collection.find(query)

if __name__ == '__main__':
    print("MongoClient imported successfully!")
    #Crear base de datos llamada mi app
    #database = client['mi_app']
    #Crear coleccion llamada usuarios
    #users = database['users']
    #Crear usuario demo
    #usuario_demo = {
    #    "user": "Rodolfo Ferro",
    #    "email": "r.ferro@ugtom.mx"
    #}
    #users.insert_one(usuario_demo)
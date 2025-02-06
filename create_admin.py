from pymongo import MongoClient
from werkzeug.security import generate_password_hash
try:
    from config import Config
except ImportError:
    from config import Config

def create_admin():
    client = MongoClient(f'mongodb://{Config.MONGODB_HOST}:{Config.MONGODB_PORT}/')
    db = client[Config.MONGODB_DB]
    users_collection = db.users

    login = input("Введите логин администратора: ")
    password = input("Введите пароль администратора: ")
    
    if users_collection.find_one({'login': login}):
        print("Пользователь с таким логином уже существует")
        return
    
    hashed_password = generate_password_hash(password)
    users_collection.insert_one({
        'login': login,
        'password': hashed_password,
        'admin': True
    })
    print(f"Администратор {login} успешно создан")

if __name__ == "__main__":
    create_admin()

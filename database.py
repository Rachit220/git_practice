from config import Config
def connect_db():
    return {
        "host": Config.get("database.host"),
        "port": Config.get("database.port"),
        "user": Config.get("database.user"),
        "password": Config.get("database.password"),
        "database": Config.get("database.name"),
    }

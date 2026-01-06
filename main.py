from config import Config
from database import connect_db

def main():
    Config.load()

    print("App Name:", Config.get("app.name"))
    print("Environment:", Config.get("app.env"))
    print("Debug Mode:", Config.get("app.debug"))

    db = connect_db()
    print("Database Config:", db)

if __name__ == "__main__":
    main()

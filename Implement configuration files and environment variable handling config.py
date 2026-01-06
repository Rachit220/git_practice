import os
import yaml
from dotenv import load_dotenv

class Config:
    _config = {}
    
    @classmethod
    def load(cls, config_path="config/config.yaml"):
        load_dotenv()
        with open(config_path, "r") as file:
            cls._config = yaml.safe_load(file)
        cls._override_with_env()
        cls._validate()

    @classmethod
    def _override_with_env(cls):
        cls._config["app"]["debug"] = os.getenv(
            "DEBUG",
            cls._config["app"]["debug"]
        ) == "True"

        cls._config["database"]["password"] = os.getenv(
            "DB_PASSWORD",
            cls._config["database"]["password"]
        )

        cls._config["app"]["env"] = os.getenv(
            "APP_ENV",
            "production"
        )

    @classmethod
    def _validate(cls):
        if not cls._config["database"]["password"]:
            raise ValueError("Database password is missing!")

    @classmethod
    def get(cls, key_path, default=None):
        keys = key_path.split(".")
        value = cls._config
        for key in keys:
            value = value.get(key)
            if value is None:
                return default
        return value


import os 


from dotenv import load_dotenv, find_dotenv

from .errors import ConfigNotFoundError


def get_env() -> bool:
    env_path = find_dotenv(".env")
    if env_path:
        load_dotenv(env_path)
        return True
    else:
        return False


if get_env():
    SPARK_URL = os.getenv("SPARK_URL")
    SPARK_API_ID = os.getenv("SPARK_APPID")
    SPARK_API_SECRET = os.getenv("SPARK_API_SECRET")
    SPARK_API_KEY = os.getenv("SPARK_API_KEY")
    SPARK_DOMAIN = os.getenv("SPARK_DOMAIN")

    YI_KEY = os.getenv("YI_KEY")

    MONGO_URI = os.getenv("MONGO_URI")
else:
    raise ConfigNotFoundError

import os

from data import spark_api
from utils.errors import ConfigNotFoundError
from utils.config import get_config


def test_chat():
    if get_config():
        spark_config = {
        "SPARK_URL": os.getenv("SPARK_URL"),
        "SPARK_API_ID": os.getenv("SPARK_APPID"),
        "SPARK_API_SECRET": os.getenv("SPARK_API_SECRET"),
        "SPARK_API_KEY": os.getenv("SPARK_API_KEY"),
        "SPARK_DOMAIN": os.getenv("SPARK_DOMAIN")
        } 
        result = spark_api.chat(spark_config, "什么是rss订阅", debug=True)
        print(result)
    else:
        raise ConfigNotFoundError
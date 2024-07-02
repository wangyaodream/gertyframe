import os

from data import spark_api
from utils import config


def test_chat():
    spark_config = {
    "SPARK_URL": config.SPARK_URL,
    "SPARK_API_ID": config.SPARK_API_ID,
    "SPARK_API_SECRET": config.SPARK_API_SECRET,
    "SPARK_API_KEY": config.SPARK_API_KEY,
    "SPARK_DOMAIN": config.SPARK_DOMAIN
    } 
    print(spark_config)
    result = spark_api.chat(spark_config, "什么是rss订阅", debug=True)
    return result

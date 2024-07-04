import os
import pprint

from dotenv import load_dotenv

from data import spark_api
from ui import gradio_ui
from utils import config


def main():
    load_dotenv()
    spark_config = {
            "SPARK_URL": config.SPARK_URL,
            "SPARK_API_ID": config.SPARK_API_ID,
            "SPARK_API_SECRET": config.SPARK_API_SECRET,
            "SPARK_API_KEY": config.SPARK_API_KEY,
            "SPARK_DOMAIN": config.SPARK_DOMAIN
            }

    message_content = "请给我一些json的测试数据"

    result = spark_api.chat(spark_config, message_content)
    return result


def gui_launch():
    gradio_ui.run()
    

if __name__ == "__main__":
    gui_launch()



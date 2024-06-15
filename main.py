import os
import pprint

from dotenv import load_dotenv

from data import spark_api
from ui import gradio_ui


def main(debug=False):
    load_dotenv()
    spark_config = {
            "SPARK_URL": os.getenv("SPARK_URL"),
            "SPARK_API_ID": os.getenv("SPARK_APPID"),
            "SPARK_API_SECRET": os.getenv("SPARK_API_SECRET"),
            "SPARK_API_KEY": os.getenv("SPARK_APIKEY"),
            "SPARK_DOMAIN": os.getenv("SPARK_DOMAIN")
            }

    message_content = "请给我一些json的测试数据"

    result = spark_api.chat(spark_config, message_content, debug=debug)
    print(result.generations)
    print(result.llm_output)
    pprint.pp(result.dict())


def test():
    gradio_ui.run()
    

if __name__ == "__main__":
    main(debug=True)



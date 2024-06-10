import os

from dotenv import load_dotenv

from data import spark_api


def main():
    load_dotenv()
    spark_config = {
            "SPARK_URL": os.getenv("SPARK_URL"),
            "SPARK_API_ID": os.getenv("SPARK_APPID"),
            "SPARK_API_SECRET": os.getenv("SPARK_API_SECRET"),
            "SPARK_API_KEY": os.getenv("SPARK_APIKEY"),
            "SPARK_DOMAIN": os.getenv("SPARK_DOMAIN")
            }

    message_content = "请给我一些json的测试数据"

    result = spark_api.chat(spark_config, message_content)
    print(result.generations[0][0].text)
    

if __name__ == "__main__":
    main()


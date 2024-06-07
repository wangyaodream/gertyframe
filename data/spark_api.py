from typing import List

from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

def chat(spark_config, message_content):
    spark = ChatSparkLLM(
            spark_api_url=spark_config["SPARK_URL"],
            spark_app_id=spark_config["SPARK_API_ID"],
            spark_api_key=spark_config["SPARK_API_KEY"],
            spark_api_secret=spark_config["SPARK_API_SECRET"],
            spark_llm_domain=spark_config["SPARK_DOMAIN"],
            streaming=False
    )

    messages: List = [ChatMessage(role="user", content=message_content)]

    handler = ChunkPrintHandler()
    if messages:
        a = spark.generate([messages], callbacks=[handler])
        return a
    else:
        return None

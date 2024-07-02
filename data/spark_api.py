from typing import List

from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage


def chat(spark_config, message_content, debug=False):
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
        # TODO 需要将结果进行保存，展示的结果只需要text值即可
        if debug:
            return a
        else:
            return a.generations[0][0].text
    else:
        return None


def message_handler(item):
    result = {}

    run_id = item["run"]["run_id"]
    llm_info = {
        ""
    }



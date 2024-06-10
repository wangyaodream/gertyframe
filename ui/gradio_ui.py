import os

import gradio as gr
from dotenv import load_dotenv, find_dotenv

from data import spark_api


def chat(content):
    # 获取config,find_dotenv()方法会向父级目录寻找.env文件
    load_dotenv(find_dotenv())

    spark_config = {
        "SPARK_URL": os.getenv("SPARK_URL"),
        "SPARK_API_ID": os.getenv("SPARK_APPID"),
        "SPARK_API_SECRET": os.getenv("SPARK_API_SECRET"),
        "SPARK_API_KEY": os.getenv("SPARK_APIKEY"),
        "SPARK_DOMAIN": os.getenv("SPARK_DOMAIN")
    }
    result = spark_api.chat(spark_config, content)
    return result


def run():
    demo = gr.Interface(
        fn=chat,
        inputs=[gr.TextArea()],
        outputs=gr.Markdown(),
    )
    demo.launch()


if __name__ == "__main__":
    run()

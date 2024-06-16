import os

import gradio as gr
from dotenv import load_dotenv, find_dotenv

from data import spark_api


def chat(content, history):
    # 获取config,find_dotenv()方法会向父级目录寻找.env文件
    load_dotenv(find_dotenv())

    history = history or []

    spark_config = {
        "SPARK_URL": os.getenv("SPARK_URL"),
        "SPARK_API_ID": os.getenv("SPARK_APPID"),
        "SPARK_API_SECRET": os.getenv("SPARK_API_SECRET"),
        "SPARK_API_KEY": os.getenv("SPARK_APIKEY"),
        "SPARK_DOMAIN": os.getenv("SPARK_DOMAIN")
    }
    result = spark_api.chat(spark_config, content)
    # TODO 需要让api也传递上下文
    history.append((content, result))
    return "", history


def run():
    chatbot = gr.Chatbot()
    # demo = gr.Interface(
    #     chat,
    #     ["text", "state"],
    #     [chatbot, "state"],
    #     allow_flagging="never",
    # )
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot(
            [],
            elem_id="chatbot",
            bubble_full_width=False
        )
        msg = gr.Textbox()

        msg.submit(
            chat,
            [msg, chatbot],
            [msg, chatbot]
        )
    demo.launch()


if __name__ == "__main__":
    run()

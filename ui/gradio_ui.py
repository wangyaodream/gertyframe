import os

import gradio as gr
from dotenv import load_dotenv, find_dotenv

from data import spark_api


def chat(content, chatbot):
    # 获取config,find_dotenv()方法会向父级目录寻找.env文件
    load_dotenv(find_dotenv())

    chatbot.append((content, ""))

    full_response = ""
    response = ""

    spark_config = {
        "SPARK_URL": os.getenv("SPARK_URL"),
        "SPARK_API_ID": os.getenv("SPARK_APPID"),
        "SPARK_API_SECRET": os.getenv("SPARK_API_SECRET"),
        "SPARK_API_KEY": os.getenv("SPARK_APIKEY"),
        "SPARK_DOMAIN": os.getenv("SPARK_DOMAIN")
    }
    result = spark_api.chat(spark_config, content)

    if result:
        for message in result:
            if message:
                response += message
                chatbot[-1] = (content, response)
                yield message
    else:
        return None


def run():
    # chatbot = gr.Chatbot(label="Chatbot", elem_classes="control-height")
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
        msg = gr.Textbox(lines=2, label="Input")
        task_history = gr.State([])

        with gr.Row():
            empty_btn = gr.Button("Clear History")
            submit_btn = gr.Button("Submit")
            regen_btn = gr.Button("Regenerate")

        submit_btn.click(chat, [msg, chatbot], [chatbot])

        # msg.submit(
        #     chat,
        #     [msg, chatbot],
        #     [msg, chatbot]
        # )
    demo.launch()


if __name__ == "__main__":
    run()

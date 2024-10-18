import gradio as gr
from zhipuai import ZhipuAI
import time
from utils.config import BIGMODEL_KEY

# 初始化ZhipuAI客户端
client = ZhipuAI(api_key=BIGMODEL_KEY)  # 请替换为你的API Key


# 定义聊天函数
def chat_with_zhipuai(message, history):
    # 构建消息历史
    messages = [{"role": "user", "content": msg[0]} for msg in history]
    messages.append({"role": "user", "content": message})

    # 调用ZhipuAI的API
    response = client.chat.completions.create(
        model="glm-4-flash",  # 使用的模型名称
        messages=messages,
        stream=True  # 启用流式输出
    )

    # 处理流式输出
    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content:
            partial_message += chunk.choices[0].delta.content
            history[-1][1] = partial_message
            yield history


def run():
    # 创建Gradio界面
    with gr.Blocks() as demo:
        gr.Markdown("# 智谱AI聊天机器人")
        chatbot = gr.Chatbot()
        msg = gr.Textbox(placeholder="请输入你的问题")
        clear = gr.Button("清除聊天记录")

        def user(message, history):
            return "", history + [[message, None]]

        def bot(history):
            return chat_with_zhipuai(history[-1][0], history)

        msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
            bot, chatbot, chatbot
        )
        clear.click(lambda: None, None, chatbot, queue=False)

    # 启动Gradio应用
    demo.launch()

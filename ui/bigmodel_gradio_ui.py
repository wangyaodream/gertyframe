import gradio as gr
from zhipuai import ZhipuAI
from utils.config import BIGMODEL_KEY


def respond(message, chat_history):
    client = ZhipuAI(api_key=BIGMODEL_KEY)
    chat_history.append((message, None))
    response = client.chat.completions.create(
            model="glm-4-flash",
            messages=[{"role": "user", "content": message}],
            stream=True
    )

    for chunk in response:
        for choice in chunk.choices:
            if content := choice.delta.content:
                breakpoint()
                chat_history[-1][1] = content
                yield chat_history
    return chat_history


def run():
    with gr.Blocks() as demo:
        gr.Markdown("<h1>Welcome</h1>")
        chatbot = gr.Chatbot()
        msg = gr.Textbox(placeholder="Please input your message...")
        clear = gr.Button("Clear")

        msg.submit(respond, [msg, chatbot], [msg, chatbot], queue=False)
        clear.click(lambda: None, None, chatbot, queue=False)

        demo.launch()

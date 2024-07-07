
import gradio as gr
from openai import OpenAI

from data import yi_api


# def call_llm_api(message):
#     completion = client.chat.completions.create(
#         model="yi-spark",
#         messages=[{'role': 'user', 'content': message}],
#         stream=True
#     )
#     return completion


def run():

    with gr.Blocks() as demo:
        chatbot = gr.Chatbot()
        msg = gr.Textbox()
        clear = gr.Button("Clear")

        def user(user_message, history):
            return "", history + [[user_message, None]]

        def bot(history):
            user_message = history[-1][0]
            bot_message = yi_api.chat(user_message)
            history[-1][1] = ""
            for chunk in bot_message:
                history[-1][1] += chunk.choices[0].delta.content or ""
                yield history

        msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
            bot, chatbot, chatbot
        )
        clear.click(lambda: None, None, chatbot, queue=False)

    demo.queue()
    demo.launch()


if __name__ == "__main__":
    run()


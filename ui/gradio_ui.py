import gradio as gr


def chat(resp):
    if isinstance(resp, dict):
        if "data" in resp:
            return resp["data"]
        else:
            return None
    elif isinstance(resp, str):
        return resp


def run():
    demo = gr.Interface(
        fn=chat,
        inputs=[gr.TextArea()],
        outputs="text",
    )
    demo.launch()


if __name__ == "__main__":
    run()

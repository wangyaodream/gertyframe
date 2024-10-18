from httpx import stream
from zhipuai import ZhipuAI
from utils.config import BIGMODEL_KEY


def zhipu_chat():
    client = ZhipuAI(api_key=BIGMODEL_KEY)
    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=[
            {"role": "user", "content": "你好！你是谁？"},
            ],
        stream=True,
    )

    for chunk in response:
        print(chunk.choices[0].delta.content)


if __name__ == "__main__":
    zhipu_chat()



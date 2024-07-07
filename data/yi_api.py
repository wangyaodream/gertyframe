import os

import openai
from openai import OpenAI

from utils import config


API_BASE = "https://api.lingyiwanwu.com/v1"


def chat(message):
    client = openai.OpenAI(
        api_key=config.YI_KEY,
        base_url=API_BASE
    )
    completion = client.chat.completions.create(
        model="yi-spark",
        messages=[{'role': "user", "content": message}],
        stream=True
    )
    return completion


if __name__ == '__main__':
    # TODO 尝试带上历史上下文来做请求
    msg = "请告诉我go中的context是什么"
    chat(msg)

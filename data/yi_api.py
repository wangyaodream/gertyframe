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
        messages=[{'role': "user", "content": message}]
    )
    return completion


if __name__ == '__main__':
    msg = "请告诉我什么是YI模型"
    result = chat(msg)
    print(result.dict())

import argparse
import sys
import os

# 获取当前脚本所在目录的绝对路径
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# 获取项目根目录的绝对路径
PROJECT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))


def init_env_user():
    pass


def init_env_config():
    # TODO 后期需要可视化界面来进行配置和添加
    env_content = """\
SPARK_APPID=""
SPARK_API_SECRET=""
SPARK_API_KEY=""
SPARK_URL="wss://spark-api.xf-yun.com/v1.1/chat"
SPARK_DOMAIN="general"

YI_KEY=""

MONGO_URI=""
"""
    env_file_path = os.path.join(PROJECT_DIR, '.env')
    with open(env_file_path, 'w', encoding='utf-8') as fp:
        fp.write(env_content)
    print(".env 文件创建成功！")


def main():

    parser = argparse.ArgumentParser(
        prog="initializing configuration"
    )

    parser.add_argument(
        "--filetype",
        choices=["env", "user"],
        help="选择一个配置文件类型 env user",
        required=True
    )

    args = parser.parse_args()

    if args.filetype == "env":
        init_env_config()
if __name__ == "__main__":
    main()

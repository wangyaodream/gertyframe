
from dotenv import load_dotenv, find_dotenv


def get_config() -> bool:
    env_path = find_dotenv(".env")
    if env_path:
        load_dotenv(env_path)
        return True
    else:
        return False

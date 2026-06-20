from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")


settings = Settings()
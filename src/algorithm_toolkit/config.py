import os

from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv(
    "APP_NAME",
    "algorithm_toolkit"
)

DEBUG = os.getenv(
    "DEBUG",
    "False"
) == "True"


LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)
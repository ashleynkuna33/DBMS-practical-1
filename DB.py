# team name: code warriors
# student numbers: 4363144, 4429119, 4346572, 4426381, 4323138, 4323584
# filename: DB.py

import os
from pathlib import Path

import pymysql
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().with_name(".env"))


def get_connection():
    required = ("DB_HOST", "DB_PORT", "DB_USER", "DB_PASSWORD", "DB_NAME")
    missing = [name for name in required if not os.getenv(name)]

    if missing:
        raise ValueError(f"Missing database configuration: {', '.join(missing)}")

    try:
        port = int(os.environ["DB_PORT"])
    except ValueError as error:
        raise ValueError("DB_PORT must be a valid integer.") from error

    if not 1 <= port <= 65535:
        raise ValueError("DB_PORT must be between 1 and 65535.")

    return pymysql.connect(
        host=os.environ["DB_HOST"],
        port=port,
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False,
        connect_timeout=10,
    )

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


class Database:

    def __init__(self):

        self.database_url = (
            f"postgresql+psycopg2://"
            f"{os.getenv('DB_USER')}:"
            f"{os.getenv('DB_PASSWORD')}@"
            f"{os.getenv('DB_HOST')}:"
            f"{os.getenv('DB_PORT')}/"
            f"{os.getenv('DB_NAME')}"
        )

        self.engine = create_engine(
            self.database_url,
            pool_pre_ping=True
        )

    def get_engine(self):
        return self.engine
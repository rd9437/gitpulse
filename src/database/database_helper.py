from sqlalchemy import text

from database.db import engine


class DatabaseHelper:

    @staticmethod
    def execute(query, params=None):

        with engine.begin() as connection:

            connection.execute(
                text(query),
                params or {}
            )

    @staticmethod
    def execute_many(query, rows):

        if not rows:
            return

        with engine.begin() as connection:

            connection.execute(
                text(query),
                rows
            )

    @staticmethod
    def fetch_all(query, params=None):

        with engine.connect() as connection:

            result = connection.execute(
                text(query),
                params or {}
            )

            return result.fetchall()

    @staticmethod
    def truncate(table_name):

        with engine.begin() as connection:

            connection.execute(
                text(
                    f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE"
                )
            )
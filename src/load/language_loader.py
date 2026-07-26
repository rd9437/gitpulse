from sqlalchemy import text

from database.db import Database


class LanguageLoader:

    def __init__(self):

        self.engine = Database().get_engine()

    def load(self, languages):

        if not languages:
            print("No languages found.")
            return

        insert_query = """

        INSERT INTO languages (

            github_repo_id,
            language,
            bytes_of_code

        )

        VALUES (

            :github_repo_id,
            :language,
            :bytes_of_code

        )

        ON CONFLICT (snapshot_date, github_repo_id, language)

        DO NOTHING

        """

        with self.engine.begin() as connection:

            connection.execute(
                text(insert_query),
                languages
            )

        print(f"Loaded {len(languages)} languages.")
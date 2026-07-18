from sqlalchemy import text

from database.db import Database


class ContributorLoader:

    def __init__(self):

        self.engine = Database().get_engine()

    def load(self, contributors):

        if not contributors:
            print("No contributors found.")
            return

        insert_query = """
        INSERT INTO contributors (

            github_contributor_id,
            github_repo_id,
            login,
            contributions,
            account_type

        )

        VALUES (

            :github_contributor_id,
            :github_repo_id,
            :login,
            :contributions,
            :account_type

        )
        """

        with self.engine.begin() as connection:

            connection.execute(
                text(insert_query),
                contributors
            )

        print(f"Loaded {len(contributors)} contributors.")
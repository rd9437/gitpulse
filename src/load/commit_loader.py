from sqlalchemy import text

from database.db import Database


class CommitLoader:

    def __init__(self):

        self.engine = Database().get_engine()

    def load(self, commits):

        insert_query = """
        INSERT INTO commits (

            github_repo_id,
            sha,
            author_name,
            author_email,
            commit_message,
            commit_date

        )

        VALUES (

            :github_repo_id,
            :sha,
            :author_name,
            :author_email,
            :commit_message,
            :commit_date

        )
        """

        with self.engine.begin() as connection:

            connection.execute(
                text(insert_query),
                commits
            )

        print(f"Loaded {len(commits)} commits.")
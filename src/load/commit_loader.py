from sqlalchemy import text

from database.db import Database


class CommitLoader:

    def __init__(self):

        self.engine = Database().get_engine()

    def load(self, commits):

        if not commits:
            print("No commits found.")
            return

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

        ON CONFLICT (snapshot_date, sha)

        DO UPDATE SET

            github_repo_id = EXCLUDED.github_repo_id,
            author_name = EXCLUDED.author_name,
            author_email = EXCLUDED.author_email,
            commit_message = EXCLUDED.commit_message,
            commit_date = EXCLUDED.commit_date,
            fetched_at = CURRENT_TIMESTAMP

        """

        with self.engine.begin() as connection:

            connection.execute(
                text(insert_query),
                commits
            )

        print(f"Loaded {len(commits)} commits.")
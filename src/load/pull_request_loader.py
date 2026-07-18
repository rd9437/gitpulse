from sqlalchemy import text

from database.db import Database


class PullRequestLoader:

    def __init__(self):

        self.engine = Database().get_engine()


    def load(self, pull_requests):

        if not pull_requests:
            print("No pull requests found.")
            return


        insert_query = """

        INSERT INTO pull_requests (

            github_pr_id,
            github_repo_id,
            title,
            state,
            merged,
            created_at,
            updated_at,
            closed_at

        )

        VALUES (

            :github_pr_id,
            :github_repo_id,
            :title,
            :state,
            :merged,
            :created_at,
            :updated_at,
            :closed_at

        )

        """


        with self.engine.begin() as connection:

            connection.execute(
                text(insert_query),
                pull_requests
            )


        print(f"Loaded {len(pull_requests)} pull requests.")
from sqlalchemy import text

from database.db import Database


class IssueLoader:

    def __init__(self):

        self.engine = Database().get_engine()

    def load(self, issues):

        if not issues:
            print("No issues found.")
            return

        insert_query = """

        INSERT INTO issues (

            github_issue_id,
            github_repo_id,
            title,
            state,
            comments,
            created_at,
            updated_at,
            closed_at

        )

        VALUES (

            :github_issue_id,
            :github_repo_id,
            :title,
            :state,
            :comments,
            :created_at,
            :updated_at,
            :closed_at

        )

        ON CONFLICT (snapshot_date, github_issue_id)

        DO NOTHING

        """

        with self.engine.begin() as connection:

            connection.execute(
                text(insert_query),
                issues
            )

        print(f"Loaded {len(issues)} issues.")
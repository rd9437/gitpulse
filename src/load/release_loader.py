from sqlalchemy import text

from database.db import Database


class ReleaseLoader:

    def __init__(self):

        self.engine = Database().get_engine()

    def load(self, releases):

        if not releases:
            print("No releases found.")
            return

        insert_query = """

        INSERT INTO releases (

            github_release_id,
            github_repo_id,
            tag_name,
            name,
            draft,
            prerelease,
            published_at

        )

        VALUES (

            :github_release_id,
            :github_repo_id,
            :tag_name,
            :name,
            :draft,
            :prerelease,
            :published_at

        )

        ON CONFLICT (snapshot_date, github_release_id)

        DO NOTHING

        """

        with self.engine.begin() as connection:

            connection.execute(
                text(insert_query),
                releases
            )

        print(f"Loaded {len(releases)} releases.")
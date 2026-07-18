from database.db import Database
from sqlalchemy import text

class RepositoryLoader:

    def __init__(self):

        self.engine = Database().get_engine()

    def load(self, data):

        repositories = data["repositories"]
        topics = data["topics"]

        with self.engine.begin() as connection:

            # -----------------------------
            # Load repositories
            # -----------------------------

            repository_query = """
            INSERT INTO repositories (

                github_repo_id,
                owner,
                name,
                full_name,
                description,
                language,
                stars,
                forks,
                watchers,
                open_issues,
                default_branch,
                visibility,
                license,
                created_at,
                updated_at

            )

            VALUES (

                :github_repo_id,
                :owner,
                :name,
                :full_name,
                :description,
                :language,
                :stars,
                :forks,
                :watchers,
                :open_issues,
                :default_branch,
                :visibility,
                :license,
                :created_at,
                :updated_at

            )
            """

            connection.execute(
                text(repository_query),
                repositories
            )


            # -----------------------------
            # Load repository topics
            # -----------------------------

            topic_query = """
            INSERT INTO repository_topics (

                github_repo_id,
                topic

            )

            VALUES (

                :github_repo_id,
                :topic

            )
            """

            connection.execute(
                text(topic_query),
                topics
            )


        print(f"Loaded {len(repositories)} repositories.")
        print(f"Loaded {len(topics)} topics.")
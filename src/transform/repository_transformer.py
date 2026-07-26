import json
from pathlib import Path


class RepositoryTransformer:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.input_dir = (
            self.project_root
            / "data"
            / "raw"
            / "repositories"
        )

    def transform(self):

        repositories = []
        topics = []

        for file in self.input_dir.glob("*.json"):

            with open(file, "r", encoding="utf-8") as f:
                repo = json.load(f)

            repositories.append({

                "github_repo_id": repo["id"],

                "owner": repo["owner"]["login"],

                "name": repo["name"],

                "full_name": repo["full_name"],

                "description": repo["description"],

                "language": repo["language"],

                "stars": repo["stargazers_count"],

                "forks": repo["forks_count"],

                "watchers": repo["subscribers_count"],

                "open_issues": repo["open_issues_count"],

                "default_branch": repo["default_branch"],

                "visibility": repo["visibility"],

                "license": (
                    repo["license"]["name"]
                    if repo["license"]
                    else None
                ),

                "created_at": repo["created_at"],

                "updated_at": repo["updated_at"]

            })

            for topic in repo.get("topics", []):

                topics.append({

                    "github_repo_id": repo["id"],

                    "topic": topic

                })

        return {

            "repositories": repositories,

            "topics": topics

        }
import json
from pathlib import Path

from transform.base_transformer import BaseTransformer


class CommitTransformer(BaseTransformer):

    def __init__(self):

        super().__init__()

        self.input_dir = (
            self.project_root
            / "data"
            / "raw"
            / "commits"
        )

    def transform(self):

        commits = []

        for file in self.input_dir.glob("*.json"):

            owner, repo = file.stem.split("_", 1)

            github_repo_id = self.get_repository_id(
                owner,
                repo
            )

            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            for commit in data:

                commits.append({
                    "github_repo_id": github_repo_id,

                    "sha": commit["sha"],

                    "author_name": (
                        commit["commit"]["author"]["name"]
                    ),

                    "author_email": (
                        commit["commit"]["author"]["email"]
                    ),

                    "commit_message": (
                        commit["commit"]["message"]
                    ),

                    "commit_date": (
                        commit["commit"]["author"]["date"]
                    )
                })

        return commits
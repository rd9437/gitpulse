import json
from pathlib import Path

from transform.base_transformer import BaseTransformer


class PullRequestTransformer(BaseTransformer):

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.input_dir = (
            self.project_root
            / "data"
            / "raw"
            / "pull_requests"
        )

    def transform(self):

        pull_requests = []

        for file in self.input_dir.glob("*.json"):

            owner, repo = file.stem.split("_", 1)

            github_repo_id = self.get_repository_id(
                owner,
                repo
            )

            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            for pr in data:

                pull_requests.append({

                    "github_pr_id": pr["id"],

                    "github_repo_id": github_repo_id,

                    "title": pr.get("title"),

                    "state": pr.get("state"),

                    "merged": pr.get("merged", False),

                    "created_at": pr.get("created_at"),

                    "updated_at": pr.get("updated_at"),

                    "closed_at": pr.get("closed_at")

                })

        return pull_requests
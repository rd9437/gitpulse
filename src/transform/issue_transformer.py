import json
from pathlib import Path

from transform.base_transformer import BaseTransformer


class IssueTransformer(BaseTransformer):

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.input_dir = (
            self.project_root
            / "data"
            / "raw"
            / "issues"
        )

    def transform(self):

        issues = []

        for file in self.input_dir.glob("*.json"):

            owner, repo = file.stem.split("_", 1)

            github_repo_id = self.get_repository_id(
                owner,
                repo
            )

            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            for issue in data:

                # Ignore pull requests stored in issues API
                if "pull_request" in issue:
                    continue

                issues.append({

                    "github_issue_id": issue["id"],

                    "github_repo_id": github_repo_id,

                    "title": issue.get("title"),

                    "state": issue.get("state"),

                    "comments": issue.get("comments"),

                    "created_at": issue.get("created_at"),

                    "updated_at": issue.get("updated_at"),

                    "closed_at": issue.get("closed_at")

                })

        return issues
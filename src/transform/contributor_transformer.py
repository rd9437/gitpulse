import json
from pathlib import Path

from transform.base_transformer import BaseTransformer


class ContributorTransformer(BaseTransformer):

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.input_dir = (
            self.project_root
            / "data"
            / "raw"
            / "contributors"
        )

    def transform(self):

        contributors = []

        for file in self.input_dir.glob("*.json"):

            owner, repo = file.stem.split("_", 1)

            github_repo_id = self.get_repository_id(
                owner,
                repo
            )

            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            for contributor in data:

                contributors.append({

                    "github_repo_id": github_repo_id,

                    "github_contributor_id": contributor["id"],

                    "login": contributor["login"],

                    "contributions": contributor["contributions"],

                    "account_type": contributor["type"]

                })

        return contributors
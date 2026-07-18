import json
from pathlib import Path

from transform.base_transformer import BaseTransformer


class ReleaseTransformer(BaseTransformer):

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.input_dir = (
            self.project_root
            / "data"
            / "raw"
            / "releases"
        )

    def transform(self):

        releases = []

        for file in self.input_dir.glob("*.json"):

            owner, repo = file.stem.split("_", 1)

            github_repo_id = self.get_repository_id(
                owner,
                repo
            )

            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            for release in data:

                releases.append({

                    "github_release_id": release["id"],

                    "github_repo_id": github_repo_id,

                    "tag_name": release["tag_name"],

                    "name": release["name"],

                    "draft": release["draft"],

                    "prerelease": release["prerelease"],

                    "published_at": release["published_at"]

                })

        return releases
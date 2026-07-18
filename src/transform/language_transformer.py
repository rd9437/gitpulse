import json
from pathlib import Path

from transform.base_transformer import BaseTransformer


class LanguageTransformer(BaseTransformer):

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

        self.input_dir = (
            self.project_root
            / "data"
            / "raw"
            / "languages"
        )

    def transform(self):

        languages = []

        for file in self.input_dir.glob("*.json"):

            owner, repo = file.stem.split("_", 1)

            github_repo_id = self.get_repository_id(
                owner,
                repo
            )

            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            for language, bytes_of_code in data.items():

                languages.append({

                    "github_repo_id": github_repo_id,

                    "language": language,

                    "bytes_of_code": bytes_of_code

                })

        return languages
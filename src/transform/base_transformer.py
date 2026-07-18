import json
from pathlib import Path


class BaseTransformer:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[2]

    def get_repository_id(self, owner, repo):

        repository_file = (
            self.project_root
            / "data"
            / "raw"
            / "repositories"
            / f"{owner}_{repo}.json"
        )

        with open(repository_file, "r", encoding="utf-8") as f:

            repository = json.load(f)

        return repository["id"]
import json
from pathlib import Path

from extract.github_client import GitHubClient


class BaseExtractor:

    endpoint = ""
    output_folder = ""

    def __init__(self):
        self.client = GitHubClient()

        self.project_root = Path(__file__).resolve().parents[2]

        self.config_file = (
            self.project_root
            / "config"
            / "repositories.json"
        )

        self.output_dir = (
            self.project_root
            / "data"
            / "raw"
            / self.output_folder
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

    def load_repositories(self):

        with open(
            self.config_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def save_json(
        self,
        owner,
        repo,
        data
    ):

        output_file = (
            self.output_dir
            / f"{owner}_{repo}.json"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    def fetch(self, owner, repo):

        endpoint = (
            f"/repos/{owner}/{repo}/{self.endpoint}"
            if self.endpoint
            else f"/repos/{owner}/{repo}"
        )

        if self.endpoint == "":
            return self.client.get(endpoint)

        return self.client.get_all_pages(
            endpoint,
            params=self.params
        )

    def extract(self):

        repositories = self.load_repositories()

        print(f"\nFound {len(repositories)} repositories.\n")

        success = 0
        failed = 0

        for repository in repositories:

            owner = repository["owner"]
            repo = repository["repo"]

            print(f"Fetching {owner}/{repo}...")

            try:

                data = self.fetch(owner, repo)

                self.save_json(
                    owner,
                    repo,
                    data
                )

                success += 1

                print("✓ Saved")

            except Exception as e:

                failed += 1

                print(f"✗ {owner}/{repo}")
                print(e)

        print("\nExtraction Summary")
        print("----------------------------")
        print(f"Successful : {success}")
        print(f"Failed     : {failed}")
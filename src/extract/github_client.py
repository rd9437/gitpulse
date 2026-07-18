import os
import time
import requests

from dotenv import load_dotenv

load_dotenv()


class GitHubClient:
    """
    GitHub REST API Client
    """

    BASE_URL = "https://api.github.com"

    def __init__(self):

        self.token = os.getenv("GITHUB_TOKEN")

        if not self.token:
            raise ValueError("GITHUB_TOKEN not found in .env")

        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28"
        }

    def get(self, endpoint, params=None):

        url = f"{self.BASE_URL}{endpoint}"

        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def get_all_pages(self, endpoint, params=None):
        """
        Fetch all pages from a paginated GitHub endpoint.
        """

        if params is None:
            params = {}

        params["per_page"] = 100

        page = 1

        all_data = []

        while True:

            params["page"] = page

            print(f"   Page {page}")

            data = self.get(endpoint, params)

            if not data:
                break

            if isinstance(data, list):
                all_data.extend(data)
            else:
                return data

            if len(data) < 100:
                break

            page += 1

            # Small delay to avoid hitting API limits
            time.sleep(0.2)

        return all_data
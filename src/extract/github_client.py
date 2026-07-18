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

        self.per_page = int(os.getenv("PER_PAGE", 100))
        self.max_pages = int(os.getenv("MAX_PAGES", 10))
        self.max_retries = int(os.getenv("MAX_RETRIES", 3))
        self.request_delay = float(os.getenv("REQUEST_DELAY", 0.2))

        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "X-GitHub-Api-Version": "2022-11-28"
        }

    def get(self, endpoint, params=None):

        url = f"{self.BASE_URL}{endpoint}"

        attempt = 0

        while attempt < self.max_retries:

            try:

                response = requests.get(
                    url,
                    headers=self.headers,
                    params=params,
                    timeout=30
                )

                # Rate limit reached
                if (
                    response.status_code == 403
                    and response.headers.get("X-RateLimit-Remaining") == "0"
                ):

                    reset = int(
                        response.headers.get(
                            "X-RateLimit-Reset",
                            time.time() + 60
                        )
                    )

                    wait_time = max(
                        reset - int(time.time()),
                        1
                    )

                    print(
                        f"Rate limit reached. "
                        f"Waiting {wait_time}s..."
                    )

                    time.sleep(wait_time)

                    continue

                response.raise_for_status()

                return response.json()

            except requests.exceptions.RequestException as e:

                attempt += 1

                if attempt >= self.max_retries:
                    raise e

                sleep_time = 2 ** attempt

                print(
                    f"Retry {attempt}/{self.max_retries}"
                    f" after {sleep_time}s..."
                )

                time.sleep(sleep_time)

    def get_all_pages(self, endpoint, params=None):
        """
        Fetch all pages from a paginated endpoint.
        """

        if params is None:
            params = {}

        params = params.copy()

        params["per_page"] = self.per_page

        page = 1

        all_data = []

        while page <= self.max_pages:

            params["page"] = page

            print(f"   Page {page}")

            data = self.get(
                endpoint,
                params=params
            )

            if not data:
                break

            if isinstance(data, list):

                all_data.extend(data)

            else:
                return data

            if len(data) < self.per_page:
                break

            page += 1

            time.sleep(self.request_delay)

        return all_data
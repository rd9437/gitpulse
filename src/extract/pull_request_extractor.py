from extract.base_extractor import BaseExtractor


class PullRequestExtractor(BaseExtractor):

    endpoint = "pulls"

    output_folder = "pull_requests"

    params = {
        "state": "all"
    }
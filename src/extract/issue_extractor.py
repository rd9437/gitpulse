from extract.base_extractor import BaseExtractor


class IssueExtractor(BaseExtractor):

    endpoint = "issues"

    output_folder = "issues"

    params = {
        "state": "all"
    }
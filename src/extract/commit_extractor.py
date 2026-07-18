from extract.base_extractor import BaseExtractor


class CommitExtractor(BaseExtractor):

    endpoint = "commits"

    output_folder = "commits"
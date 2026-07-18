from extract.base_extractor import BaseExtractor


class ReleaseExtractor(BaseExtractor):

    endpoint = "releases"

    output_folder = "releases"
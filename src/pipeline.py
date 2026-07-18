from extract.repository_extractor import RepositoryExtractor
from extract.contributor_extractor import ContributorExtractor
from extract.commit_extractor import CommitExtractor
from extract.issue_extractor import IssueExtractor
from extract.language_extractor import LanguageExtractor
from extract.pull_request_extractor import PullRequestExtractor
from extract.release_extractor import ReleaseExtractor


class ETLPipeline:

    def run(self):

        print("=" * 60)
        print("GitPulse ETL Pipeline")
        print("=" * 60)

        extractors = [
            RepositoryExtractor(),
            ContributorExtractor(),
            CommitExtractor(),
            IssueExtractor(),
            LanguageExtractor(),
            PullRequestExtractor(),
            ReleaseExtractor(),
        ]

        for extractor in extractors:

            print(f"\nRunning {extractor.__class__.__name__}...\n")

            extractor.extract()

        print("\n" + "=" * 60)
        print("ETL Pipeline Completed Successfully")
        print("=" * 60)
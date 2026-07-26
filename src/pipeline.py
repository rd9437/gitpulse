from extract.repository_extractor import RepositoryExtractor
from transform.repository_transformer import RepositoryTransformer
from load.repository_loader import RepositoryLoader

from extract.contributor_extractor import ContributorExtractor
from transform.contributor_transformer import ContributorTransformer
from load.contributor_loader import ContributorLoader

from extract.commit_extractor import CommitExtractor
from transform.commit_transformer import CommitTransformer
from load.commit_loader import CommitLoader

from extract.issue_extractor import IssueExtractor
from transform.issue_transformer import IssueTransformer
from load.issue_loader import IssueLoader

from extract.language_extractor import LanguageExtractor
from transform.language_transformer import LanguageTransformer
from load.language_loader import LanguageLoader

from extract.pull_request_extractor import PullRequestExtractor
from transform.pull_request_transformer import PullRequestTransformer
from load.pull_request_loader import PullRequestLoader

from extract.release_extractor import ReleaseExtractor
from transform.release_transformer import ReleaseTransformer
from load.release_loader import ReleaseLoader


class ETLPipeline:

    def run(self):

        print("=" * 60)
        print("GitPulse ETL Pipeline")
        print("=" * 60)

        jobs = [

            (
                "Repositories",
                RepositoryExtractor(),
                RepositoryTransformer(),
                RepositoryLoader()
            ),

            (
                "Contributors",
                ContributorExtractor(),
                ContributorTransformer(),
                ContributorLoader()
            ),

            (
                "Commits",
                CommitExtractor(),
                CommitTransformer(),
                CommitLoader()
            ),

            (
                "Issues",
                IssueExtractor(),
                IssueTransformer(),
                IssueLoader()
            ),

            (
                "Languages",
                LanguageExtractor(),
                LanguageTransformer(),
                LanguageLoader()
            ),

            (
                "Pull Requests",
                PullRequestExtractor(),
                PullRequestTransformer(),
                PullRequestLoader()
            ),

            (
                "Releases",
                ReleaseExtractor(),
                ReleaseTransformer(),
                ReleaseLoader()
            )

        ]

        for name, extractor, transformer, loader in jobs:

            print("\n" + "=" * 60)
            print(f"{name}")
            print("=" * 60)

            print("\n[1/3] Extracting...")
            extractor.extract()

            print("\n[2/3] Transforming...")
            transformed_data = transformer.transform()

            print("\n[3/3] Loading...")
            loader.load(transformed_data)

        print("\n" + "=" * 60)
        print("GitPulse ETL Pipeline Completed Successfully")
        print("=" * 60)
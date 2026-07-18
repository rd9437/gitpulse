from transform.issue_transformer import IssueTransformer
from load.issue_loader import IssueLoader


transformer = IssueTransformer()

loader = IssueLoader()


issues = transformer.transform()

loader.load(issues)


print("\nIssue ETL completed successfully!")
from ingest import load
from validate import check
from ledger import record

data = load()

for item in data:
    issues = check(item)
    block = record({"data": item, "issues": issues})
    print(block)

import json

def load(path="data/feed.json"):
    with open(path) as f:
        return json.load(f)

# create a small program to pull a random wikipedia article from a specific topic

import requests

def fetch_categories(prefix, limit=10):
    endpoint = "https://en.wikipedia.org/w/api.php"
    parameters = {
        "action": "query",
        "list": "allcategories",
        "acprefix": prefix, # the prefix to search for
        "format": "json",
        "aclimit": limit # how many categories to pull
    }

    response = requests.get(endpoint, params=parameters)
    data = response.json()

    categories = [category["*"] for category in data["query"]["allcategories"]]
    return categories
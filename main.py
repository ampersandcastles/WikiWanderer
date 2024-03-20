# create a small program to pull a random wikipedia article from a specific topic

import requests

def get_random_wikipedia_article():
    endpoint = "https://en.wikipedia.org/w/api.php"
    parameters = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnnamespace": 0, # 0 is the main namespace
        "rnlimit": 1 # how many random articles to pull
    }

    response = requests.get(url=endpoint, params=parameters)
    data = response.json()

    random_article_title = data["query"]["random"][0]["title"]
    random_article_url = f"https://en.wikipedia.org/wiki/{random_article_title.replace(' ', '_')}"

    return random_article_title, random_article_url

title, url = get_random_wikipedia_article()
print(f"Random Wikipedia article: {title}\nURL: {url}")
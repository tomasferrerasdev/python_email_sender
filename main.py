""" This module is the main module of the project """

import requests

URL = (
    "https://newsapi.org/v2/everything"
    "?q=python&sortBy=publishedAt&pageSize=2&apiKey=9c5d9a849ad8406298f2c719023f9c59"
)
req = requests.get(URL, timeout=5)

# Get dictionary from json
content = req.json()

# Access the article
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

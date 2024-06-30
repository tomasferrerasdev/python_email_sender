""" This module is the main module of the project """

import os
import requests
from email_sender import send_email

os.environ["KEY"] = "9c5d9a849ad8406298f2c719023f9c59"

TOPIC = "tesla"
URL = (
    "https://newsapi.org/v2/everything"
    f"?q={TOPIC}&sortBy=publishedAt&language=en&apiKey={os.environ["KEY"]}"
)
req = requests.get(URL, timeout=5)

# Get dictionary from json
content = req.json()

# Access the article
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = f"Subject: Today's {TOPIC} news" + "\n" + body + article["title"] + "\n" + str(article["description"]) + "\n" + str(article["url"]) + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)

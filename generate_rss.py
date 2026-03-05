import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator

url = "https://www.zaanschemolen.nl/nieuws/"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

fg = FeedGenerator()
fg.title("Website RSS")
fg.link(href=url)
fg.description("Automatisch gemaakte RSS feed")

for link in soup.select("a"):
    title = link.text.strip()
    href = link.get("href")

    if title and href:
        fe = fg.add_entry()
        fe.title(title)
        fe.link(href=href)

rss = fg.rss_str(pretty=True)

with open("feed.xml", "wb") as f:
    f.write(rss)

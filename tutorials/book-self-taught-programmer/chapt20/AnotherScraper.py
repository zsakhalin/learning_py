import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        r = urllib.request.urlopen(self.url) # return site's html-code with adress url
        html = r.read() # html has site's code
        parser = "html.parser"
        sp = BeautifulSoup(html, parser) # parses html-code
        with open('urls', 'w') as f:
            for tag in sp.find_all("a"):
                url = tag.get("href")
                if url is None:
                    continue
                else:
                    if "./articles" in url:
                        url = "https://news.google.com" + url.replace(".", "")
                        f.write(url + "\n")
                        print(f"\n {url}")

print("In progress...")
url: str = "https://news.google.com/"
Scraper(url).scrape()
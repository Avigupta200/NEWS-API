import requests
from termcolor import colored

class News:
    def __init__(self):
        self.api = "YOUR_API_KEY_HeRE"

    def get_news(self):
        query = input("What type of news are you interested in today? ")

        url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={self.api}"

        r = requests.get(url)
        data = r.json()

        articles = data["articles"]

        for index, article in enumerate(articles):
            print(index + 1, colored(article["title"], attrs=["bold"]))
            print("To read the article:", article["url"])
            print("\n************************************\n")

news1 = News()
news1.get_news()

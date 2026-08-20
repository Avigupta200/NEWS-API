import requests
from termcolor import colored 

query = input("What type of news are you interested in today? ")
api = "YOUR API KEY HERE" 

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-07-20&sortBy=publishedAt&apiKey={api}"


print(url)
r =  requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, colored(article["title"], attrs=['bold']))
    print("To read the article: ", article["url"])
    print("\n****************************************\n")

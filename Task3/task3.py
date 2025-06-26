import requests
from bs4 import BeautifulSoup

url = "https://www.ndtv.com/news"

page = requests.get(url)


soup = BeautifulSoup(page.content, "html.parser")

headlines = soup.find_all("h3")

file = open("headlines.txt", "w", encoding="utf-8")


for i, headline in enumerate(headlines, start=1):
    text = headline.get_text().strip()
    if len(text) > 10:  
        file.write(f"{i}. {text}\n")

file.close()
print(" Headlines saved to headlines.txt")

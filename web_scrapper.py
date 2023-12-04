from bs4 import BeautifulSoup
import requests

url = "https://healthwatchline.com"

req = requests.get(url)
soup = BeautifulSoup(req.content, 'lxml')
titles = soup.find_all("h2", {"class":"post_title"})

titles = titles[0].getText()

for title in titles:
    print(title.getText())

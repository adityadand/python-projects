from bs4 import BeautifulSoup
import urllib3
import requests

url = requests.get("http://www.reddit.com")

soup = BeautifulSoup(url.content,'html.parser')
soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))

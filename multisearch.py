import requests , sys, webbrowser, bs4
from bs4 import BeautifulSoup
query = input("Enter query to search ")
webbrowser.open('https://google.com/search?q='+query)
webbrowser.open('https://www.linkedin.com/search/results/all/?keywords='+query)
webbrowser.open('https://www.facebook.com/search/top/?q='+query)
webbrowser.open('https://www.youtube.com/results?search_query='+query)
webbrowser.open('https://en.wikipedia.org/wiki/'+query)
webbrowser.open('https://www.instagram.com/'+query)
webbrowser.open('https://twitter.com/search?q='+query)
webbrowser.open('https://www.google.com/search?tbm=isch&source=hp&biw=559&bih=754&ei=-OL8W_zMH8Gl9QOkxoKwCQ&q='+query)
webbrowser.open('https://www.reddit.com/search?q='+query)
webbrowser.open('https://in.search.yahoo.com/search?p='+query)
webbrowser.open('https://www.bing.com/search?q='+query)
webbrowser.open('https://duckduckgo.com/?q='+query)
webbrowser.open('https://www.quora.com/search?q='+query)
webbrowser.open('https://in.pinterest.com/search/pins/?q='+query)




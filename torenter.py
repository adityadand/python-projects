#find books easily
import requests , sys, webbrowser, bs4
from bs4 import BeautifulSoup
# an tool to search torrent files on multiple torrent sites
print("torenter - vpn required")
query = input("search torrent files in multiple torrent sites")
webbrowser.open('https://idope.se/torrent-list/'+query)
webbrowser.open('http://1337x.am/search/'+query+'/1/')
webbrowser.open('https://unblockpirate.uk/search.php?q='+query)
webbrowser.open('https://zooqle.com/search?q='+query)
webbrowser.open('https://yts.lt/browse-movies/'+query)
webbrowser.open('https://www.torlock2.com/all/torrents/'+query+'.html?')
webbrowser.open('https://extratorrent.si/search/?search='+query+'&new=1&x=0&y=0')







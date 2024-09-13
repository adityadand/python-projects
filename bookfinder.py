#find people information
import requests , sys, webbrowser, bs4
from bs4 import BeautifulSoup
query = input("Enter query to find books ")
webbrowser.open('http://libgen.is/search.php?req='+query)
webbrowser.open('https://www.barnesandnoble.com/s/'+query)
webbrowser.open('http://gen.lib.rus.ec/search.php?req='+query)
webbrowser.open('http://b-ok.cc/s/?q='+query)
webbrowser.open('https://www.bookfinder.com/search/?author=&title='+query)
webbrowser.open('https://archive.org/details/texts?and%5B%5D='+query)
webbrowser.open('https://www.gutenberg.org/ebooks/search/?query='+query)
webbrowser.open('http://www.freebookspot.es/default.aspx')
webbrowser.open('https://www.free-ebooks.net/search/'+query)
webbrowser.open('https://www.google.com/search?domains=www.ebooklobby.com&q='+query)
webbrowser.open('https://openlibrary.org/search?q='+query)
webbrowser.open('http://www.freebookcentre.net/search.html?cx=partner-pub-9069158947264549%3Ar8chyjx6rk2&cof=FORID%3A10&ie=ISO-8859-1&q='+query)
webbrowser.open('http://ebook3000.info/searching/page1.html')
webbrowser.open('https://www.google.com/search?ei=aSIfXPmzBYeFvQSBxamABA&q=pdf:%20'+query)



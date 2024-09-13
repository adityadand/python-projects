import webbrowser
import requests
from bs4 import BeautifulSoup

def search_book(query):
    search_engines = [
        ("Libgen", "http://libgen.is/search.php?req="),
        ("Barnes & Noble", "https://www.barnesandnoble.com/s/"),
        ("Gen.lib.rus.ec", "http://gen.lib.rus.ec/search.php?req="),
        # ... add more search engines here
    ]

    for name, url in search_engines:
        try:
            webbrowser.open(url + query)
        except Exception as e:
            print(f"Error searching {name}: {e}")

def main():
    query = input("Enter query to find books: ")
    search_book(query)

if __name__ == "__main__":
    main()

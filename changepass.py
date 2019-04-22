import requests , sys, webbrowser, bs4
from bs4 import BeautifulSoup

print("a tool to change multiple social accounts password you must be logged in before")
webbrowser.open('https://www.facebook.com/settings?tab=security&section=password&view')
webbrowser.open('https://myaccount.google.com/security')
webbrowser.open('https://twitter.com/settings/password')
webbrowser.open('https://www.quora.com/settings')
webbrowser.open('https://github.com/settings/admin')
webbrowser.open('https://www.instagram.com/accounts/password/change/')
webbrowser.open('https://www.linkedin.com/psettings/change-password')

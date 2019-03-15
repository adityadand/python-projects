import requests , sys, webbrowser, bs4
from bs4 import BeautifulSoup
query = input("Enter website to scan ")
webbrowser.open(query)
webbrowser.open('https://sitecheck.sucuri.net/results/'+query)
webbrowser.open('https://www.whois.com/whois/'+query)
webbrowser.open('https://www.ssllabs.com/ssltest/analyze.html?d='+query)
webbrowser.open('https://app.upguard.com/webscan#/'+query)
webbrowser.open('https://www.spyfu.com/overview/domain?query='+query)
webbrowser.open('https://app.buzzsumo.com/research/content?type=articles&result_type=total&num_days=365&general_article&infographic&video&how_to_article&list&what_post&why_post&q='+query)
webbrowser.open('https://web.archive.org/web/*/'+query)
webbrowser.open('site:'+query)




 
  
  
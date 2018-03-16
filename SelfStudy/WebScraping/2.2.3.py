__author__ = 'tanmch791115'
# coding=utf-8

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, 'html.parser')
""" for child in bsObj.find('table',{'id':'giftList'}).children:
    print(child) """
""" for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sibling) """
print(bsObj.find('img', {'src': "../img/gifts/img1.jpg"}
                 ).parent.previous_sibling.get_text())

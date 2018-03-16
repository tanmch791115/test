__author__ = 'tanmch791115'
# coding=utf-8
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, 'html.parser')
images=bsObj.findAll('img',{'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
for image in images:
    # print(image['src'])
    print(image.attrs['src'])
tags=bsObj.findAll(lambda tag: len(tag.attrs)==2)
for tag in tags:
    print(tag)

__author__ = 'tanmch791115'
# coding=utf-8

from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj=BeautifulSoup(html,'html.parser')
nameList=bsObj.findAll('span',{'class':['green']})
for name in nameList:        
    print(name.get_text())
nameList=bsObj.findAll(text='the prince')
print(len(nameList))
allText=bsObj.findAll(id='text')
print(allText[0].get_text())
print(bsObj.h1)

    

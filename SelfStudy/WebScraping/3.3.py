__author__ = 'tanmch791115'
# coding=utf-8

from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages=set()
random.seed(datetime.datetime.now())

#获取页面所有内链的页面
def getInternalLinks(bsObj,includUrl):
    includUrl=urlparse(includUrl).scheme+'://'+urlparse(includUrl).netloc
    internalLinks=[]
    #找出所有以"/"开头的链接
    for link  in bsObj.findAll('a',href=re.compile('^(/|.*'+includUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startwith('/')):
                    internalLinks.append(includUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks


    
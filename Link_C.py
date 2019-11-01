#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 12:52:51 2019

@author: manzars
"""

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

url = "https://mclloydbis.com/manufactures-directory-index-"

req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')  

alpha = [chr(x) for x in range(97, 123)]
links = []

for alp in alpha:
  link = url + alp + "-page-"
  for i in range(1, 1000):
    inner_link = link + str(i) + ".html"
    req = requests.get(inner_link)
    soup = BeautifulSoup(req.text, 'lxml')
    tab = soup.findAll('div', {'class': 'listSummary'})
    para = tab[1].findAll('a')[::4]
    for p in para:
      links.append(urljoin(inner_link, p.attrs['href']))
    li = soup.findAll('ul', {'class': 'PagingList'})[0].findAll('li')
    try:
      print(li[-1].a.attrs['href'])
    except:
      print('here')
      break
  
with open('links.txt', 'w') as f:
    for link in links:
        f.write(str(link) + "\n")
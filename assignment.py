#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 12:30:59 2019

@author: manzars
"""

import pandas
from bs4 import BeautifulSoup
import requests

links = []
with open('links.txt', 'r') as f:
    for line in f:
        links.append(str(line.strip()))
'''
file = open('data.csv', 'a')
header = "Name, Address, Telephone, Mobile, Fax, Email, Website, Contact person\n"
file.write(header) 
file.close()
'''

for link in links[len(pandas.read_csv('data.csv')) : ]:
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'lxml')
    name = soup.findAll('h2')[0].text
    table = soup.findAll('tr', {'class': 'even'})
    x = table[0].strong.text.lstrip().rstrip().split()
    address = " ".join(x)
    p = table[0].contents[-2].text.rstrip().rstrip().strip().split('\n')
    data = [x.replace('\xa0', '').replace('N/A', 'NaN') for x in p]
    print(name, data)
    file = open('data.csv', 'a')
    file.write(name.replace(',', '') + ', ' + address.replace(',', '') + ', ' +  data[0] + ', ' + data[1] + ', ' + data[2] + ', ' + data[3] + ', ' + data[4] + ', ' + data[5] + '\n')
    file.close()
    
#!/usr/bin/python3

import requests
import numpy as np
from bs4 import BeautifulSoup

data = input('Enter the keyword you want to search:- ')

url = 'https://www.google.com/search?q='+data

wiki = requests.get(url)
soup = BeautifulSoup(wiki.text,'html.parser')


# to show the page in an indented way
#print(soup.prettify())

links = soup.select('div > h3 > a')
links1 = soup.select('cite')

ans=[]	# for getting the text of every cite link
x=[]

for i in range(0,len(links)):
	abc = links[i].get('href')
	loc = 0
	loc = abc.find('https')
	x.append(abc[loc:])

for i in range(0,len(links1)):
	ans.append(links1[i].getText())


# to get the youtube link
for i in range(0,len(ans)):
	if ans[i].find('youtube')!=-1:
		x.append(ans[i])

for i in range(0,len(x)):
	print(x[i])



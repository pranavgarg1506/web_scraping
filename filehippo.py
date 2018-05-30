#!/usr/bin/python3

import os
from bs4 import BeautifulSoup
import requests
import numpy as np

url='https://filehippo.com/'

wiki = requests.get(url)
soup = BeautifulSoup(wiki.text,'html.parser')

#print(soup.prettify())


# to select the popular software from filehippo.com
section = soup.select('div > div > ul[id=popular-list] > li > a')

unstriped_text=[]  # 
striped_text=[]

for i in range(0,len(section)):
	#print(np.size(section[i].getText()))
	unstriped_text.append(section[i].getText())	#________________ to get the text from the section______________
	striped_text.append(unstriped_text[i].strip())	#_________________ too get the striped text___________
	#print(len(striped_text[i]))
	print(striped_text[i])				#_____________ to print the list_______________________


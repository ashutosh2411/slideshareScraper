import urllib
import time
import os
import sys
from os import listdir
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Firefox()
url = 'https://www.slideshare.net/anniyappa/dbms-an-example'
folder = 'images/'
driver.get(url)
source = driver.page_source
soup = BeautifulSoup(source, 'lxml')
elem = soup.findAll(True, {'class':['slide_image']})
driver.quit()
l = []
count = 1
file = [f for f in listdir(folder)]
for f in file:
	os.remove(folder+f)

print len(elem)
for i in elem :
	t = str(i)
	t = t[t.find('data-full')+11:]
	temp = t[:t.find('"')]
	l.append(temp)
	urllib.urlretrieve(temp, folder + str(count).zfill(3)+".jpg")
	count = count + 1
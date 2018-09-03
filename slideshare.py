import urllib
from threading import *
import time
import os
import sys
from os import listdir
from bs4 import BeautifulSoup
from selenium import webdriver

def download(temp, folder, count):
	urllib.urlretrieve(temp, folder + str(count)+".jpg")

driver = webdriver.Firefox()
url = 'https://www.slideshare.net/aziz_khan/paleolithic-and-neolithic'
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
	thread = Thread(target=download, args=[temp ,folder, count])
	thread.start()
	count = count + 1


import urllib2
from bs4 import BeautifulSoup
import csv
baseurl = 'http://www.planecrashinfo.com'
dburl = 'http://www.planecrashinfo.com/database.htm'
page = urllib2.urlopen(dburl)
soup = BeautifulSoup(page)
linki = soup.findAll("a")
links = linki.get('href')
for lin in [:-1]:
    url = baseurl + lin
    so = BeautifulSoup(urllib2.urlopen(url)
    

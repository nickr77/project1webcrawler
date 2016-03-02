__author__ = 'Nick Roberts -- Steven Bock'

import re
import mechanize
from BeautifulSoup import BeautifulSoup
#Needs to return: list of pages, list of outgoing links, amount of JPG files, save words from .txt .htm .html files, stem words before storing in list/dictionary

browse = mechanize.Browser()
#CONFIG SECTION
browse.set_handle_robots(True)

#END CONFIG SECTION
#GLOBAL VARS
baseUrl = "http://lyle.smu.edu/~fmoore"
urlList = [baseUrl]
visitedUrls = [baseUrl]
retrieveLimit = 0
stopWords = []
links = []
outgoingLinks = []
jpgAmount = 0
words = {}

#END GLOBAL VARS

browse.open(baseUrl)
soup = BeautifulSoup(browse.response().read())
wordsInPage = soup.getText().split()
for x in wordsInPage:
    print x




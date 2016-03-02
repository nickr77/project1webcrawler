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
badLinks = []
jpgAmount = 0
words = {}

#END GLOBAL VARS
stopFile = open("stopwords.txt", "r")
lines = stopFile.read()
stopWords = lines.split()

for page in urlList:

    visitedUrls.append(page)


    browse.open(page)
    soup = BeautifulSoup(browse.response().read())
    wordsInPage = soup.getText().split()

    #get all links, check if in list already or visited
    #make sure urls are actually different
    #count jpgs
    #if link doesn't work, add to badLinks list





    for x in wordsInPage: #parse and stem words, add to dictionary
        if x not in stopWords:
            print x




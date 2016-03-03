__author__ = 'Nick Roberts -- Steven Bock'

import re
import mechanize
import urlparse
import robotparser
from BeautifulSoup import BeautifulSoup
#Needs to return: list of pages, list of outgoing links, amount of JPG files, save words from .txt .htm .html files, stem words before storing in list/dictionary

browse = mechanize.Browser()
#CONFIG SECTION
#browse.set_handle_robots(True)

#END CONFIG SECTION
#GLOBAL VARS
baseUrl = "http://lyle.smu.edu/~fmoore/"
robots = robotparser.RobotFileParser()
robots.set_url(urlparse.urljoin(baseUrl, "robots.txt"))
robots.read()
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

print robots.path
print robots.can_fetch("*", "/dontgohere/")
print robots.can_fetch("*", "/dontgohere/index.html")


temp = input("Enter page limit: ")
retrieveLimit = int(temp)
stopFile = open("stopwords.txt", "r")
lines = stopFile.read()
stopWords = lines.split()

for page in urlList:

    #print page, "CHECK1"

    visitedUrls.append(page)

    try:
        browse.open(page)
        soup = BeautifulSoup(browse.response().read())
        wordsInPage = soup.getText().split()
        for link in browse.links():
            tempURL = urlparse.urljoin(link.base_url, link.url)
            if tempURL not in urlList:

                #print link
                if tempURL.startswith(baseUrl):
                    if robots.can_fetch("*", "/" + link.url):
                        print "WE CAN FETCH IT ", tempURL
                        urlList.append(tempURL)
                    else:
                        print "We can't fetch it: ", tempURL
                else:
                    outgoingLinks.append(tempURL)

        #get all links, check if in list already or visited
        #make sure urls are actually different
        #count jpgs
        #if link doesn't work, add to badLinks list
        for x in wordsInPage: #parse and stem words, add to dictionary
            if x not in stopWords:
                temp = x
    except:
        print "Couldn't open that link", page



__author__ = 'Nick Roberts -- Steven Bock'

import re
import mechanize
import urlparse
import robotparser
from BeautifulSoup import BeautifulSoup
from string import digits
import snowballstemmer
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
stopWords = ()
outgoingLinks = []
badLinks = []
jpgAmount = 0
words = {}
docIDCounter = 1
documentIDs = []
stemmer = snowballstemmer.stemmer("english")
#END GLOBAL VARS
temp = input("Enter page limit: ")
retrieveLimit = int(temp)
stopFile = open("stopwords.txt", "r")
lines = stopFile.read()
stopWords = lines.split()

print "Crawling Pages, please wait..."
for page in urlList:
    if docIDCounter > retrieveLimit:
        break
    #visitedUrls.append(page)

    try:
        browse.open(page)
        soup = BeautifulSoup(browse.response().read()) #if can't parse, assumed to be binary file or 404
        wordsInPage = soup.getText().split()
        for link in browse.links():
            tempURL = urlparse.urljoin(link.base_url, link.url)
            #BELOW: gets rid of duplicate urls resulting from index.html/index.htm
            if tempURL.endswith("index.html"):
                tempURL = tempURL.replace("index.html", "")
            elif tempURL.endswith("index.htm"):
                tempURL = tempURL.replace("index.htm", "")


            if tempURL not in urlList:
                if tempURL.startswith(baseUrl):
                    if robots.can_fetch("*", "/" + link.url):
                        #print "WE CAN FETCH IT ", tempURL
                        urlList.append(tempURL)
                else:
                    if tempURL + "/" not in urlList:
                        outgoingLinks.append(tempURL)

        documentIDs.append((docIDCounter, page))

        for x in wordsInPage: #parse and stem words, add to dictionary
            x = x.replace(",", "") #removes commas before checking for stopwords
            x = re.sub("[^a-zA-Z]","", x)
            if x not in stopWords and len(x) > 0:# and not set('[~=!@-<>#$%^&*()_+{}":;\']+$').intersection(x): #gets rid of invalid words
                temp = x
                temp = temp.lower()
                temp = stemmer.stemWord(temp)
                #print temp
                if temp not in words.keys():
                    words[temp] = [docIDCounter]
                else:
                    words[temp].append(docIDCounter)
        docIDCounter += 1 #increments doc ID after successful parsing


                #index words here
    except: #occurs if it is a binary file or non-existent file
        #print "Couldn't open that link", page
        if page.endswith(".jpg"):
            jpgAmount += 1
        if browse.response().code == 404:
            badLinks.append(page)
print "Computing Word frequency"
wordFreqency = []
for x in words.keys():
    wordFreqency.append((str(x), len(words[x])))
frequentWords = sorted(wordFreqency, key=lambda x: x[1])
frequentWords.reverse()

print "Most Frequent Words: ", frequentWords[:20]
print "OUTGOING LINKS: ",outgoingLinks #for debugging, remove once complete
print "Good URLS: ",urlList
print "BAD LINKS: ",badLinks
print "JPEGS: ", jpgAmount
print "DOCIDS : ", documentIDs

#FILE WRITING
out = open('urlList.txt', 'w') #page List
out.write('List of all urls visited (or at least attempted to):\n')
for x in urlList:
    out.write(x)
    out.write("\n")
out.close()

out = open('outgoingLinks.txt', 'w') #outgoing links
out.write('List of outgoing links:\n')
for x in outgoingLinks:
    out.write(x)
    out.write("\n")
out.close()

out = open('badLinks.txt', 'w') #bad links
out.write('List of bad links:\n')
for x in badLinks:
    out.write(x)
    out.write("\n")
out.close()



out = open('jpegAmount.txt', 'w') #amount of jpegs
out.write("JPEG AMOUNT: ")
out.write(str(jpgAmount))
out.close()

out = open('wordIndex.txt', 'w') #amount of jpegs
out.write("Word Index:\n")
for x in words.keys():
    out.write(x)
    out.write(": ")
    out.write(str(words[x]))
    out.write('\n')
out.close()

out = open('frequentWords.txt', 'w')
out.write("20 most frequent words and amount of occurences:\n")
for x in frequentWords[:20]:
    out.write(x[0])
    out.write(": ")
    out.write(str(x[1]))
    out.write('\n')
out.close()

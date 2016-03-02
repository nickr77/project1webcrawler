__author__ = 'Nick Roberts -- Steven Bock'

import re
import mechanize

browse = mechanize.Browser()
page = browse.open("http://lyle.smu.edu/~fmoore")

print page.read()
print browse.geturl()
for links in browse.links():
    print links

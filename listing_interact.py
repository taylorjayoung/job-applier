import urllib2
from bs4 import BeautifulSoup as soup
import urlparse
import mechanize
import unicodedata
import re
import numpy as np

job_id = "a0a420f3d81521c8"
url = "https://www.indeed.com/viewjob?jk=" + job_id
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
web_soup = soup(urllib2.urlopen(url),features="html5lib")
print web_soup

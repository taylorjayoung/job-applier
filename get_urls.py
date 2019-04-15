import urllib2
from bs4 import BeautifulSoup as soup
import urlparse
import mechanize
import unicodedata
import re
import numpy as np

jobs = []
displayIndex = 0
counter = 20
i = 0
while i <2:
    url = "https://www.indeed.com/jobs?q=software+developer&start=" + str(displayIndex)
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    web_soup = soup(urllib2.urlopen(url),features="html5lib")

    table = web_soup.find(name="td", attrs={'id': 'resultsCol'})
    for div in table.findAll('div'):
        try:
            if div['data-jk']:
                jobs.append(div['data-jk'])
        except:
            print "no id found"

    displayIndex += counter
    i += 1


# np.savetxt('job_ids.txt', jobs, delimiter=',', fmt='%s')

# regex = '<div class="jobsearch-SerpJobCard">(.+?)</div>'
# pattern = re.compile(regex)
#
# tds = re.findall(pattern,htmltext)
#
# print tds

# urls = [url]
# visited = [url]
# x=0
# while len(urls)>0:
#     try:
#         br.open(urls[0])
#         urls.pop(0)
#         x=x+1
#         if x > 5:
#             break
#         print br.links()
#         for link in br.links():
#             newurl = urlparse.urljoin(link.base_url, link.url)
#             b1 =  urlparse.urlparse(newurl).hostname
#             b2 =  urlparse.urlparse(newurl).path
#             newurl = "http://"+b1+b2
#
#             if newurl not in visited and urlparse.urlparse(url).hostname in newurl:
#                 urls.append(newurl)
#                 visited.append(newurl)
#
#     except:
#         urls.pop(0)
#
#






#If we use the DOM to find our job links
#On each page the job results are in an HTML table with id="pageContent"
#In the <td id="resultsCol">
    #Each listing in <div class="jobsearch-SerpJobCard unifiedRow row result clickcard">
        #Div has a <div class="title">
            #<a href="LINK TO JOB LISTING">


#http:// + base_url + company specs + job specs
#base_url  = indeed.com/

#company specs = cmp/(companyName)/

#job specs = jobs/ + job title
#job title = Junior-Software-Engineer-e678625aaf65b7ab?q=software+developer&vjs=3

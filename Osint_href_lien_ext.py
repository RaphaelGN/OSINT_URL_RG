from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from Osint_href_Exterieure import *


# Collects a list of all external URLs found on the site
allExtLinks = set()
allIntLinks = set()


def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)

    domain = "{}://{}".format(urlparse(siteUrl).scheme, urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, "html.parser")

    internalLinks = getInternalLinks(bs, domain)

    externalLinks = getExternalLinks(bs, domain)
    print(internalLinks)

    try:
        for link in externalLinks:
            if link not in allExtLinks:
                allExtLinks.add(link)
                print(link)
        for link in internalLinks:
            if link not in allIntLinks:
                allIntLinks.add(link)
                getAllExternalLinks(link)

    except AttributeError:
        print("encore pas fou??")

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


def voidTitle(title):
    if title == None:
        print("Pas de titre trouvé")
    else:
        print(title)

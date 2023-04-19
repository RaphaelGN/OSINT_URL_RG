from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import numpy as np

pages = set()


def get_All_URL(url):
    global pages

    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    images = bs.find_all(
        "img",
    )

    toto = []
    try:
        for link in bs.find_all("a", href=re.compile("^()")):
            if "href" in link.attrs:
                toto.append(link.attrs["href"])
    except AttributeError:
        print("Probleme page sécurité sans doute?!")

    return toto

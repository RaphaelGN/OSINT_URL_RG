from Osint_titre import *
from Osint_href import *
from Osint_href_Exterieure import *
from Osint_sauvergarde import *
from Osint_href_lien_ext import *

# dans le dossier cd osint-1234-R_G
# pour lancer l'application  python all_function.py dans le terminal du

URL_page = "https://www.ece.fr/"


def main():
    try:
        print(URL_page)
        title = getTitle(URL_page)
        voidTitle(title)

        print("start-------------------")
        toto = get_All_URL(URL_page)
        print("end --------------------")

        transformation_text_sauvergarde(toto)
        try:
            getAllExternalLinks(URL_page)  ## encore quelque faute
        except AttributeError:
            print("trop beau pas fou de chez fou mais? ")

        try:
            print("hhello")
        # followExternalOnly(URL_page)
        except AttributeError:
            print("pas fou de chez fou? ")
    except AttributeError:
        print("pas fou, URL? ")
    return True


main()

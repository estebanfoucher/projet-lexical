from requests import *
from bs4 import BeautifulSoup

def get_synonyms(word):
    url = f"https://www.cnrtl.fr/synonymie/{word}"

    html = get(url).text

    soup = BeautifulSoup(html, 'html.parser')

    L = soup.find("table", {"class":"light_frame"}).find_all("a")

    G=[]
    for elt in L:
        G.append(elt.text)

    return(G)

    

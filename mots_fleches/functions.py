from .synonyms import get_synonyms
import pandas as pd

def get_definition(word):

    df = pd.read_csv("larousse.csv", sep = "$")
    return str(df.loc[df["word"] == word].head(1)["definition"])

def order1_synonyms(string):
    str1 = string
    L = str1.split(" ")
    G = [] + L
    for word in L:
        l = get_synonyms(word)
        G += l    
    return str(G)

def takeSecond(elem):
    return elem[1]

def distance(string1, string2):
    
    str2 = purify(string2)
    str1 = purify(string1)
    set1 = set(str1.split(" "))
    set2 = set(str2.split(" "))
    return len(set1 & set2)

def purify(line):
    for char in line:
        if char in "?.,!/;:[]'":
            line = line.replace(char,'')
    return line.lower()

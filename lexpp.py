with open("lexique.csv", 'r') as csvfile:
    lexpp0 = csvfile.readlines()
    lexpp = []
    for elt in lexpp0:
        lexpp.append(elt.replace("\n", ""))

from json import dump, load

# with open("lexique.csv", 'r') as csvfile:
#     lexpp0 = csvfile.readlines()
#     lexpp = []
#     for elt in lexpp0:
#         lexpp.append(elt.replace("\n", ""))

# new_lex = list(set(lexpp))
larousse = {}

import pandas as pd

def get_definition(word):
    df = pd.read_csv("larousse.csv", sep = "$")
    return df.loc[df["word"] == word]


with open("lexique.json", "r") as jsonfile:
    lexique = load(jsonfile)
i = 0

print(len(lexique))
for word in lexique:
    larousse[word] = get_definition(word).head(1)["definition"]
    print(i)
    i+=1

with open("larousse.json", "w") as jsonfile:
    dump(larousse, jsonfile)



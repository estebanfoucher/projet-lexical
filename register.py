from larousse_api import larousse
from lexpp import lexpp

def register(word):
    definitions = larousse.get_definitions(word)
    with open('larousse.txt', "a") as csvfile:
        csvfile.write(word+"$"+str(definitions)+"\n")

for word in lexpp[:10]:
    register(word)
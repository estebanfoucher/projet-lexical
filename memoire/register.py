from larousse_api import larousse
from lexpp import lexpp

i = 30

def register(word):
    definitions = larousse.get_definitions(word)
    with open(f"larousse{i}.txt", "a") as csvfile:
        csvfile.write(word+"$"+str(definitions)+"\n")

def unregister(word):
    with open(f"failed{i}.txt", "a") as csvfile:
        csvfile.write(word+"\n")

for word in lexpp[int(i*10000):]:
    try:
        register(word)
    except:
        unregister(word)
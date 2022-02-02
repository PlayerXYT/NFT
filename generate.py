from PIL import Image
import os, random

def randimg(path):
    out = random.choice(os.listdir(path))
    return Image.open(path+out)

if random.randint(0, 100) == 0: # The rarity of the rare group is 1 in 100 by default
    imgb = randimg("./bottom/rare/")
else:
    imgb = randimg("./bottom/")

if random.randint(0, 100) == 0: # The rarity of the rare group is 1 in 100 by default
    imgm = randimg("./mid/rare/")
else:
    imgm = randimg("./mid/")

if random.randint(0, 100) == 0: # The rarity of the rare group is 1 in 100 by default
    imgt = randimg("./top/rare/")
else:
    imgt = randimg("./top/")


inter = Image.alpha_composite(imgb, imgm)
final = Image.alpha_composite(inter, imgt)
final.save("out.png")
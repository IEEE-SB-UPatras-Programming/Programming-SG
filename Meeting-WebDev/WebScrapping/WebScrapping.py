from os import EX_OSFILE
import requests
import shutil
from bs4 import BeautifulSoup

URL = "http://www.ece.upatras.gr" # Enter whatever url you want here!

#print(page.text)

page = requests.get(URL + "/index.php/el") # Add the specific page that you want to get the images from.

soup = BeautifulSoup(page.content, "html.parser")

imgs = soup.find_all("img")

print(imgs)

for l in imgs:

    img_src = URL + l["src"]
    
    fileName = l["src"].replace("/", "")
    print(fileName)

    with open("./Pics/{}".format(fileName), "wb") as imgFile:

        try:
            res = requests.get(img_src, stream = True)
            shutil.copyfileobj(res.raw, imgFile)
        except Exception as e:
            print(e)

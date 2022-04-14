import cv2
counter=0
listara=[]
listara2=[]
while True:
    counter=counter+1
    try:
        ad1=12-len(str(counter))
        ad2=ad1*"0"
        image = cv2.imread("{}{}.png".format(ad2,counter))
        pixel = image[100, 100]
        listara.append(str(pixel))
    except:
        
        break
for i in listara:
    lista3=[]
    k=i.replace("[","")
    k=k.replace("]","")
    k=k.replace("  "," ")
    k=k.strip()
    lista3=k.split()
    tel=str(int(lista3[0])//9)+str(int(lista3[1])//9)+str(int(lista3[2])//9)
    listara2.append(tel)

for i in listara2:
    print(i)

from PIL import Image, ImageDraw, ImageFont
import subprocess
import os
import time

counter = 1

t1=time.time()

# Usage: Edit Text.txt. Run this script. Watch out.mp4!

with open("Text.txt", "rb") as f:
    byte = f.read(1)

    while byte:
        
        byte=ord(byte)
        byte=str(byte)
        additive1 = 3 - len(byte)
        additive2=additive1*"0"
        byte=additive2+byte # 1 => 001, 97 => 097

        print(byte)
        
        
        img = Image.new('RGB', (256, 144), color = (int(byte[0])*9,
                                                    int(byte[1])*9,
                                                    int(byte[2])*9))
        ad1 = 12 - len(str(counter))

        ad2=ad1*"0"
        img.save("./Images/{}{}.png". format(ad2,counter))


        counter=counter+1
        
        byte = f.read(1)

t2=time.time()
f.close()
p = os.popen("ffmpeg -r 30 -pattern_type glob -i './Images/*.png' -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4 -y")
t3=time.time()
print(t2-t1)
print(t3-t2)

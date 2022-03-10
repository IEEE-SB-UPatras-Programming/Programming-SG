import re

with open("./appmanifest_240.acf") as steam_file:
    
    s = r"\"([^\"]*)\"\s*\"([^\"]*)\""

    for line in steam_file: 
        try:
            print("{} {}".format(*re.findall(s, line)[0]))
        except:
            pass



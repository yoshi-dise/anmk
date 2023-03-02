import re
import os
import requests
dick = []
with open("target.txt", "r") as f:
    titles = f.read().split("\n")[:-1]
    for title in titles:
        ttype = "new"
        newbaselink = "https://cdn.animatic.fun/PUBLIC/{title}/media/{filename}"
        oldbaselink = "https://cdn.animatic.fun/PUBLIC/{title}/media/Animatic/{filename}"
        x = title.split("-")
        for idn, y in enumerate(x):
            if(y == "part"):
                x[-2] = "P{}".format(x[-1])
                del x[-1]
            elif(re.search("p[0-9]", y) != None):
                x[-1] = x[-1].upper()
            else:
                x[idn] = y.capitalize()
        newtitle = "".join(x)
        oldtitle = " ".join(x)
        oldertitle = " ".join(x).lower().capitalize()
        x[-1] = x[-1].capitalize()
        x[-2] = x[-2].lower()
        oldertitle2 = " ".join(x).capitalize()

        print("testing "+ newbaselink.format(title=newtitle, filename="01I.mp4"))
        res = requests.get(newbaselink.format(title=newtitle, filename="01I.mp4"))
        if res.status_code == 403:
            print("testing "+ newbaselink.format(title=newtitle, filename="01L.mp4"))
            res = requests.get(newbaselink.format(title=newtitle, filename=f"01L.mp4"))
            if res.status_code == 403:
                print("testing "+ oldbaselink.format(title=oldtitle, filename="01I.mp4"))
                res = requests.get(oldbaselink.format(title=oldtitle, filename=f"01I.mp4"))
                if res.status_code == 403:
                    print("testing "+ oldbaselink.format(title=oldtitle, filename="01L.mp4"))
                    res = requests.get(oldbaselink.format(title=oldtitle, filename=f"01L.mp4"))
                    if res.status_code == 403:
                        print("testing "+ oldbaselink.format(title=oldertitle, filename="01I.mp4"))
                        res = requests.get(oldbaselink.format(title=oldertitle, filename=f"01I.mp4"))
                        if res.status_code == 403:
                            print("testing "+ oldbaselink.format(title=oldertitle, filename="01L.mp4"))
                            res = requests.get(oldbaselink.format(title=oldertitle, filename=f"01L.mp4"))
                            if res.status_code == 403:
                                print("testing "+ oldbaselink.format(title=oldertitle2, filename="01I.mp4"))
                                res = requests.get(oldbaselink.format(title=oldertitle2, filename=f"01I.mp4"))
                                if res.status_code == 403:
                                    print("testing "+ oldbaselink.format(title=oldertitle2, filename="01L.mp4"))
                                    res = requests.get(oldbaselink.format(title=oldertitle2, filename=f"01L.mp4"))
                                    if res.status_code == 403:
                                        print("unknown error, maybe the title doesnt even exist")
                                        ttype = "unknown"
                                else: ttype = "older2"
                            else:
                                ttype = "older"
                        else:
                            ttype = "older"
                    else:
                        ttype = "old"
                else:
                    ttype = "old"
            else:
                ttype = "new"
        else:
            ttype = "new"
        print(ttype)
        dick.append([title, ttype])

txt = ""
for dic in dick:
    txt = txt + dic[0] + "@" + dic[1] + "\n"
f = open("titles2.txt", "w")
f.write(txt)
f.close()
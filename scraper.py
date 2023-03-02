import requests
import re

titles = []
for iden in range(1, 8):
    print("Scraping page {}...".format(iden))
    if(iden == 1):
        link = "https://animatic.fun/category/animation/"
    else:
        link = "https://animatic.fun/category/animation/page/{}/".format(iden)
    x = requests.get(link)
    patt = re.compile('<a class="bg-link" href="(.+?)"', re.IGNORECASE)
    links = patt.findall(x.text)
    for link in links:
        titles.append(link.split("/")[-2])

print(titles)
towrite = ""
for title in titles:
    towrite = "{}{}\n".format(towrite, title)
f = open("titles.txt", "w")
f.write(towrite)
f.close()
print("Successfully saved all titles into : titles.txt\nTotal: {} titles".format(len(titles)))
import requests
import re

titles = []
links = []
for iden in range(1, 8):
    print("Scraping page {}...".format(iden))
    if(iden == 1):
        link = "https://animatic.fun/category/animation/"
    else:
        link = "https://animatic.fun/category/animation/page/{}/".format(iden)
    x = requests.get(link)
    patt = re.compile('<a class="bg-link" href="(.+?)"', re.IGNORECASE)
    y = patt.findall(x.text)
    for z in y:
        links.append(z)

print("Done scraping page, scraping titles from each page...")

for link in links:
    print(f"scraping {link} ...")
    res = requests.get(link)
    pattern = re.compile('<iframe src="(.+?)"', re.IGNORECASE)
    x = pattern.findall(res.text)[0].split("/")[-2]
    titles.append(x)

print(titles)
towrite = ""
for title in titles:
    towrite = "{}{}\n".format(towrite, title)
f = open("target.txt", "w")
f.write(towrite)
f.close()
print("Successfully saved all titles into : target.txt\nTotal: {} titles".format(len(titles)))
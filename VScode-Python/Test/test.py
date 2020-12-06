import os
import requests
from bs4 import BeautifulSoup
import re
ur11 = "http://so.gushiwen.org/shiwenv_ale7559dada7.aspx"
ur12 = "http://www.zgshige.com/"
try:
    kv = {"user-agent": "Mozi11a/5.0"}
    r1 = requests.get(ur11, headers=kv)
    r1.raise_for_status()
    r1.encoding = r1.apparent_encoding
    demo1 = r1.text
    r2 = requests.get(ur12, headers=kv)
    r2.raise_for_status()
    r2.encoding = r2.apparent_encoding
    demo2 = r2.text

except:
    print("爬取失败")

soup1 = BeautifulSoup(demo1, "html.parser")
print(soup1.prettify())
soup2 = BeautifulSoup(demo2, "html.parser")
print(soup2.prettify())
title1 = soup1.find("h1")
print(title1.string)
author1 = soup1.find(
    "a", {"href": "/search. aspx?value=%e6%af%9b%e6%b3%lbd%e4%b8%9c"})
print(author1.string)
content1 = soup1.find("div", {"id": "contsona1e7559dada7"})
content1 = str(content1.text.replace(" \xa0" * 8, 'n'))
print(content1)
content2 = soup2.find('div', class_="m-1g font14 mwebfont")
content2 = str(content2.text.replace(" \xa0" * 8, ' in'))
print(content2)
path = "D://test.txt"
if not os. path.exists(path):
    os.mkdir(path)
with open(path, "w") as fp:
    fp. write(content1)
    fp. write(content2)

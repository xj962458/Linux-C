import requests
from bs4 import BeautifulSoup

r = requests.get('https://so.gushiwen.org/shiwenv_a1e7559dada7.aspx')
soup = BeautifulSoup(r.text, 'html.parser')
ls = [{'style': 'font-size:20px; line-height:22px; height:22px; margin-bottom:10px;'}, {'class': 'source'},
      {'class': 'contson', 'id': 'contsona1e7559dada7'}]
title = soup.find('h1', ls[0]).text
author = str(soup.find('p', ls[1]).text).strip('\n')
details = str(soup.find('div', ls[2]).text).replace('。', '。\n')
a = ("{0:^22}\n".format(title) + "{0:>20}".format(author) + details).strip('\n')
print(a, end=' ')
with open('test1.txt', 'w+', encoding='utf-8') as f:
    f.write(a)

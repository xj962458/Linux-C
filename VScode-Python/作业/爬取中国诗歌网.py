import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.zgshige.com/c/2020-12-01/16034533.shtml', timeout=30)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
ls = [{'class': 'col-xs-12'}, {'style': 'font-family: 宋体, SimSun; font-size: 16px; color: rgb(0, 0, 0);'}]

title = soup.find('h3').text
author = soup.find('div', ls[0]).text.replace('\t', '').replace('\n', ' ').replace(' ', '')[:7]
detail = soup.find('span', ls[1])
a = ''
for i in detail.contents:
    a += str(i).replace('<br/>', '\n')
a = '{0:^15}\n'.format(title) + '{0:>15}\n'.format(author) + a
print(a)
with open('test2.txt', 'w+',encoding='utf-8') as f:
    f.write(a)

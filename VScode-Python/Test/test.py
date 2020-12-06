import requests
from bs4 import BeautifulSoup

r = requests.get('https://wuhu.meituan.com/',timeout=30)
r.encoding='utf-8'
soup=BeautifulSoup(r.text,'html.parser')
with open('./test.csv','w+') as f:
    for i in soup.find_all('a'):
        print(i.string,end=': ')
        print(i.attrs.get('href'))
        f.write(str(i.string)+',\t'+str(i.attrs.get('href'))+'\n')

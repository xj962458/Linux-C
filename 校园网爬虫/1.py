import requests
from bs4 import BeautifulSoup

for i in range(67,89):
    r=requests.get('https://www.ahpu.edu.cn/jsjyxxgc/5466/list{}.htm'.format(i),timeout=30)
    r.encoding='utf-8'
    soup=BeautifulSoup(r.text,'html.parser')
    with open("./test.txt",'a',encoding='utf-8') as f:
        for i in soup.find_all('a'):
            if len(str(i.attrs.get('title')))>5:
                print(i.attrs.get('title'))
                print('https://www.ahpu.edu.cn/'+i.attrs.get('href'))
                if i.attrs.get('href')[0]=='/':
                    f.write(str(i.attrs.get('title'))+'\n'+'https://www.ahpu.edu.cn'+i.attrs.get('href')+'\n')
                else:
                    f.write(str(i.attrs.get('title'))+'\n'+i.attrs.get('href')+'\n')



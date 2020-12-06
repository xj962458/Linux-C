import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/74.0.3729.169 Safari/537.36"}
r1 = requests.get('https://movie.douban.com/subject/25907124/?tag=%E7%83%AD%E9%97%A8&from=gaia_video', headers=headers)
r2 = requests.get('https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2621219978.webp', stream=True)
bs = BeautifulSoup(r1.text, "html.parser")
data = bs.find_all('span', {'class': 'short'})

a = ''
for i in data:
    a += i.text.replace('。', '。\n').replace('，', '，\n') + '\n'
print(a)
with open('text3.txt', 'w') as f1, open('test.jpg', 'wb') as f2:
    f1.write(a)
    f2.write(r2.content)

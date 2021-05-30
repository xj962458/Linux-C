import requests
import os

if not os.path.exists('image'):
    os.mkdir('image')


def parse_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/74.0.3729.169 Safari/537.36"}
    res = requests.get(url, headers=headers)
    text = res.text
    item = []
    for i in range(25):
        text = text[text.find('alt') + 3:]
        item.append(extract(text))
    return item


def extract(text):
    text = text.split('"')
    name = text[1]
    image = text[3]
    return name, image


def write_movies_file(item, stars):
    print(item)
    with open('douban_film.txt', 'a', encoding='utf-8') as f:
        f.write('排名：%d\t电影名：%s\n' % (stars, item[0]))
    r = requests.get(item[1])
    with open('image/' + str(item[0]) + '.jpg', 'wb') as f:
        f.write(r.content)


def main():
    stars = 1
    for offset in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start=' + str(offset) + '&filter='
        for item in parse_html(url):
            write_movies_file(item, stars)
            stars += 1


if __name__ == '__main__':
    main()

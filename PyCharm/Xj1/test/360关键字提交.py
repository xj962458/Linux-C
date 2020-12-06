import requests
from bs4 import BeautifulSoup
import re


def getKeywordResult(keyword):
    url = 'http://www.so.com/s?q=' + keyword
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""


def parserLinks(html):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for h3 in soup.find_all('h3', {'class': re.compile('res-title')}):
        links.append(h3.text.strip('\n'))
    return links


def main():
    html = getKeywordResult('python')
    ls = parserLinks(html)
    count = 1
    for i in ls:
        print("[{:^3}]{}".format(count, i))
        count += 1


main()

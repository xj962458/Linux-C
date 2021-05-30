import base64
import requests

session = requests.session()


def upload(locate1, locate2, confidence):
    file1 = open(locate1, 'rb')
    file2 = open(locate2, 'rb')
    image1 = base64.b64encode(file1.read())
    image2 = base64.b64encode(file2.read())
    url = ""

    session.headers = {
        "Host": "your_iot_domain",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Origin": "https://your_iot_domain/",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/70.0.3538.110 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://your_iot_domain/index.php/admin.html",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    data = {
        'image1': 'data:image/jpg;base64,' + str(image1, 'utf-8'),
        'image2': 'data:image/jpg;base64,' + str(image2, 'utf-8'),
        'confidence': confidence
    }
    res = session.post(url=url, data=data, verify=False)
    print(res.text)

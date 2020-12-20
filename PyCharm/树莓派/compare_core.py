import base64
import json
from json import JSONDecoder
import face_recognition
import requests


def submit(url, submit_data):
    response = requests.post(url, data=submit_data)
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    return req_dict


def get_access_token(client_id, client_secret):
    url = "https://aip.baidubce.com/oauth/2.0/token"
    data = {"grant_type": "client_credentials", "client_id": client_id, "client_secret": client_secret}
    response = submit(url, data)

    access_token = response['access_token']
    return access_token


def face_compare(access_token, locate1, locate2):
    url = "https://aip.baidubce.com/rest/2.0/face/v3/match" + "?access_token=" + access_token

    file1 = open(locate1, 'rb')
    file2 = open(locate2, 'rb')
    image1 = base64.b64encode(file1.read())
    image2 = base64.b64encode(file2.read())

    data = json.dumps(
        [{"image": str(image1, 'utf-8'), "image_type": "BASE64", "face_type": "CERT", "quality_control": "NONE"},
         {"image": str(image2, 'utf-8'), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "NORMAL"}])

    response = submit(url, data)
    print(response)
    if response['error_code'] != 0:
        return 0
    score = response['result']['score']
    return score


def compare_face_recognition(locate1, locate2):
    first_image = face_recognition.load_image_file(locate1)
    second_image = face_recognition.load_image_file(locate2)
    first_encoding = face_recognition.face_encodings(first_image)
    second_encoding = face_recognition.face_encodings(second_image)
    if len(first_encoding) == 0:
        return 2
    if len(second_encoding) == 0:
        return 3
    results = face_recognition.compare_faces([first_encoding][0], second_encoding[0])
    if results != "True":
        results = face_recognition.face_distance([first_encoding][0], second_encoding[0])
    return results

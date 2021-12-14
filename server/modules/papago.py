import requests
from server.KEYS import CLIENT_ID, CLIENT_PW

HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Naver-Client-Id': CLIENT_ID,
    'X-Naver-Client-Secret': CLIENT_PW,
}
str1="demo trasnslation of bbox1"

def translation_en2ko(sentence):
    data = f'source=en&target=ko&text={sentence}'
    response = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=HEADERS, data=data)
    response_json=response.json()
    return response.status_code, response_json['message']['result']['translatedText']
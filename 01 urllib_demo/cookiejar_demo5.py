from urllib.request import build_opener, HTTPCookieProcessor
from http.cookiejar import LWPCookieJar

cookie = LWPCookieJar()
cookie.load('cookie2.txt', ignore_expires=True, ignore_discard=True)
handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36')]
response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))
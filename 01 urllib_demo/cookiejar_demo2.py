from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor

cookie = CookieJar()
hander = HTTPCookieProcessor(cookie)
opener = build_opener(hander)
response = opener.open('https://www.bing.com')
for item in cookie:
    print(item.name + '=' + item.value)
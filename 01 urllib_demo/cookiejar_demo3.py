from http.cookiejar import MozillaCookieJar
from urllib.request import build_opener, HTTPCookieProcessor

filename = 'cookie.txt'
cookie = MozillaCookieJar(filename)
handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)
response = opener.open('https://www.bing.com')
cookie.save(ignore_discard=True, ignore_expires=True)
from http.cookiejar import LWPCookieJar
from urllib.request import build_opener, HTTPCookieProcessor


filename = 'cookie2.txt'
cookie = LWPCookieJar(filename)
handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)
'''
由于考虑到有些网站需要添加headers才能进行访问，
按照之前的思路，考虑的是采用Request类，但是现在因为考虑到了获取cookie。
因此通过opener来添加headers
'''
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36')]
response = opener.open('https://www.baidu.com')
cookie.save(ignore_expires=True, ignore_discard=True)
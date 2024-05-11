# coding=utf-8
import requests
from urllib.request import urlretrieve
import re

url = ('https://comic.idmzj.com/api/v1/s_comic/chapter/detail?channel=pc&app_name=comic&version=1.0.0&timestamp=1694662882598&uid&comic_py=shijiemorichaiquanweiban&chapter_id=81379')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;/'
                         ' x64) AppleWebKit/537.36 (KHTML, like/'
                         ' Gecko) Chrome/124.0.0.0 Safari/537.36'}
html = requests.get(url=url, headers=headers)
html_str = html.text.encode('utf-8').decode()
pattern = re.compile('http.*?jpg', re.S)
text = re.findall(pattern, html_str)
count = 1
for i in text:
    urlretrieve(i, f'0{count}.jpg')
    count += 1

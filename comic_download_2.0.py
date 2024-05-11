# coding=utf-8
import requests
from urllib.request import urlretrieve
import re


def get_pics(x, k):
    id = x
    chapter_url = (
        f'https://comic.idmzj.com/api/v1/s_comic/chapter/detail?channel=pc&app_name=comic&version=1.0.0&timesta/'
        f'mp=1694662882598&uid&comic_py=shijiemorichaiquanweiban&chapter_id={id}')
    pics_html = requests.get(url=chapter_url, headers=headers)
    pics_html = pics_html.text.encode('utf-8').decode()
    pics_pattern = re.compile('http.*?jpg', re.S)
    pics_url = re.findall(pics_pattern, pics_html)
    print(pics_url)
    print(len(pics_url))
    for i in pics_url:
        urlretrieve(i, f'0{k}.jpg')
        print('pics' + f'0{k}' + '下载完成')
        k += 1
    return k

url = ('https://comic.idmzj.com/api/v1/s_comic/comic/detail?channel=pc&app_name=comic&version=1.0.0&timestamp=16946628/'
       '82598&uid&comic_py=shijiemorichaiquanweiban')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124./'
                         '0.0.0 Safari/537.36'}
html = requests.get(url=url, headers=headers)
html = html.text.encode('utf-8').decode()
pattern = re.compile('chapter_id.*?chapter_title', re.S)
text = re.findall(pattern, html)
id_list = []
for i in text:
    id_num = re.findall('\\d.*\\d', i)
    id_num = id_num[0]
    id_list.insert(0, id_num)
for i in range(2):
    id_list.remove(id_list[0])
k = 1
for i in id_list:
    k = get_pics(i, k)

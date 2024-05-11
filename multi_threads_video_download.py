#   这是需要AES解密的
# encoding = utf-8
import os
import time
import requests
import re
from Crypto.Cipher import AES
from concurrent.futures import ThreadPoolExecutor


def html_collector():
    url = []
    for i in range(1, 24):
        url1 = f'https://www.yartvu.net/play/6638-1-{i}.html'
        url.append(url1)    # 获取23集全部源网页
    return url


def key_inf_collector(url):
    key = []
    for i in url:
        res = requests.get(i)
        html = str(res.text.encode('utf-8'))
        pattern = re.compile(r'play\\\\/(.*?)\\\\/index.m3u8', re.S)  # 查找23集关键信息
        key.append(re.findall(pattern, html))  # 获取23集关键信息
    return key


def video_and_key_collector(key):
    key_url = []
    video_url = []
    for i in key:
        video_url.append(f'https://v.gsuus.com/play/{i[0]}/index.m3u8')  # 获取12集视频地址
        key_url.append(f'https://v.gsuus.com/play/{i[0]}/enc.key')  # 获取12个key
    return key_url, video_url


def video_download(u, num, num1):
    print(f"第{num}集{num1}开始下载")
    content = session.get(u).content
    print(f"第{num}集{num1}content获取成功")
    with open(f'D:\\attack on titan 3\\{num}\\第{num}集{num1}.ts', 'wb') as f:
        f.write(decrypter.decrypt(content))
    print(f"第{num}集{num1}下载完成")


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124/'
                         '.0.0.0 Safari/537.36'.encode('utf-8')}  # 请求头


with ThreadPoolExecutor(50) as t:
    future = t.submit(html_collector)
    url = future.result()
    print("url获取完毕")
    future1 = t.submit(key_inf_collector, url)
    key = future1.result()
    print("key获取完毕")
    future2 = t.submit(video_and_key_collector, key)
key_url, video_url = future2.result()
idd = 1
path = 'D:\\attack on titan 3'
os.chdir(path)
start = time.time()
for i in range(23):
    key1 = requests.get(url=key_url[i], headers=headers).content
    video_list = requests.get(url=video_url[i], headers=headers).text
    pattern1 = re.compile('https.*?ts', re.S)
    video_list1 = re.findall(pattern1, str(video_list))  # 获取某集全部ts地址
    decrypter = AES.new(key=key1, mode=AES.MODE_CBC)  # 单集AES解密器构造
    id = 1
    new_folder = f'{idd}'
    os.makedirs(new_folder)
    session = requests.session()
    print(f'第{idd}集开始下载')
    with ThreadPoolExecutor(50) as t:
        for j in video_list1:
            t.submit(video_download, j, idd, id)
            id += 1
            time.sleep(1)
    print(f'第{idd}集下载完成')
    idd += 1
end = time.time()
time = end - start
print(f"全部下载完成，共用时{time}秒")

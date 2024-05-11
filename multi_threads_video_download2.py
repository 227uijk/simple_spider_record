#   无需AES解密
# encoding=utf-8
import re
import ffmpy3
import requests
from multiprocessing.dummy import Pool as Threads
from concurrent.futures import ThreadPoolExecutor
import time
import os


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124/'
                         '.0.0.0 Safari/537.36'}    # 请求头设置，伪装UI


def index_get(j):    # 获取27集m3u8视频地址
    html_url = f'https://www.yartvu.net/play/23911-2-{j}.html'  # 获取网页地址
    html_text = session.get(html_url, headers=headers).text.encode('utf-8')  # 爬取网页源代码
    pattern = re.compile(r'20220728\\\\/(.*?)\\\\/index', re.S)  # 查找index地址关键字
    index_list.append(f"https://cdn6.yzzy-online.com/20220728/{re.findall(pattern, str(html_text))[0]}/1000k" +
                      '/hls/index.m3u8')    # 获取index地址


def video_download(u):
    k = index_list.index(u) + 1
    print(f'第{k}集开始下载')
    name = f'第{k}集.mp4'
    ffmpy3.FFmpeg(inputs={u: None}, outputs={name: None}).run()
    print(f'第{k}集下载完成')


index_list = []
session = requests.session()
info = []
for i in range(1, 28):
    with ThreadPoolExecutor(80) as t:
        future1 = t.submit(index_get, i)
session = requests.session()
path = 'D://attack on titan 4'
os.chdir(path)
start = time.time()
pool = Threads(20)
results = pool.map(video_download, index_list)
pool.close()
pool.join()
end = time.time()
time = start - end
mins = time % 60
seconds = time - mins * 60
print(f"下载总耗时{mins}分{seconds}秒")

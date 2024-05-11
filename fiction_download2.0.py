# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re


def split_string(x, length):
    return [x[j:j + length] for j in range(0, len(x), length)]


def get_fiction(x, y):
    html = requests.get(url=x, headers=y)
    html.encoding = 'utf-8'
    html_str = html.text
    html = BeautifulSoup(html_str, 'lxml')
    if html.find('div', id='chaptercontent', class_="Readarea ReadAjax_content"):
        content = html.find('div', id='chaptercontent', class_="Readarea ReadAjax_content")
        content = content.text
    else:
        return "This is empty"
    pattern = re.compile('.*请', re.S)
    content = re.findall(pattern, content)
    content = ''.join(content[0].split())
    content_list = list(content)
    content_list.remove(content_list[-1])
    content = ''.join(content_list)
    return content


authority_url = 'https://www.xbqg99.com/'
headers = {'User-Agent': 'Mozilla/5.0 (/'
           'Windows NT 10.0; Win64; x64) AppleWebK/'
           'it/537.36 (KHTML, like Gecko) Chrome/1/'
           '24.0.0.0 Safari/537.36 Edg/124.0.0.0'}
url = 'https://www.xbqg99.com/book/77516/'
main_html = requests.get(url, headers=headers)
main_html = main_html.text
main_html = BeautifulSoup(main_html, 'lxml')
chapters = main_html.find('div', class_='listmain')
chapters = chapters.find_all('a')
for chapter in chapters:
    href = chapter.get('href')
    name = chapter.text
    url = authority_url + href
    text = get_fiction(url, headers)
    text = split_string(text, 50)
    with open('wzzs1.txt', 'a', encoding='utf-8') as f:
        f.write(name + '\n')
        for i in text:
            f.write(i + '\n')
        f.write('\n')
    print(name, '下载完成')
print("下载完成")

All of the spider I ve tried to make.


#  1111111
#  fiction_download_1.0
#  This is my first spider program. It was quite excited to creat one on my own. I ve just learned a week when the day I started it.
#  Followings are specific codes.


# coding=utf-8  #  This is mainly about the coding problem.
import requests
from bs4 import BeautifulSoup
import re


def split_string(x, length):  #  Creating a function to split string and better print it.
    return [x[j:j + length] for j in range(0, len(x), length)]  #  Return a list.


url = 'https://www.xbqg99.com/book/77516/11.html'  #  This is the url of the first chapter of the fiction.
headers = {'User-Agent': 'Mozilla/5.0 (Windows /'
                         'NT 10.0; Win64; x64) /'
                         'AppleWebKit/537.36 (K/'
                         'HTML, like Gecko) Chr/'
                         'ome/124.0.0.0 Safari//'
                         '537.36 Edg/124.0.0.0'}  #  Creat a fake UI.
html = requests.get(url=url, headers=headers)  #
html.encoding = 'utf-8'  #
html_str = html.text  #  Getting the html's string.
content_text = BeautifulSoup(html_str, 'lxml')  #  Transforming it into a soup.
content_text_str = content_text.find('div', id='chaptercontent', class_="Readarea ReadAjax_content")  #  Finding the element which contents text.
content_title_str = content_text.find('h1', class_='wap_none')  #  Finding the title of this chapter.
content = content_text_str.text.strip().split('  ')  #  Tiding the text.
title = content_title_str.text    #    Getting title.
print(title)
text = ''
for i in content:
    text += i
pattern = re.compile('.*请', re.S)
text = re.findall(pattern, text)
text1 = ''
for i in text:
    text1 += i
text = re.sub('\\s', '', text1)
text = split_string(text, 50)
with open('wzzs.txt', 'w') as f:
    f.write(title + '\n')
with open('wzzs.txt', 'a') as f:
    for i in text:
        print(i, end='\n')
        f.write(i + '\n')

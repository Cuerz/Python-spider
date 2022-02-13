# -*- encoding: UTF-8 -*-
#使用正则表达式获取古诗文网推荐诗文

import requests
import re
def get_poem(page):
    url = "https://www.gushiwen.cn/default_{}.aspx".format(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }
    response = requests.get(url=url,headers=headers)
    # 网页源码
    html_doc = response.text
    # 获取标题
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', html_doc, re.DOTALL)
    # 获取朝代
    dynasties = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', html_doc, re.DOTALL)
    # 获取诗人
    authors = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', html_doc, re.DOTALL)
    # 获取内容
    contents_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>', html_doc, re.DOTALL)
    contents = []
    # 遍历列表，取出每篇诗文的内容，并替换\n和标签为空
    for content in contents_tags:
        content = re.sub(r'<.*?>', '', content).replace('\n','')
        contents.append(content.strip())
    # 使用列表存储每篇诗文
    poems = []
    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = value
        poem = [
            {
                'title':title,
                'dynasty':dynasty,
                'author': author,
                'content': content
            }
        ]
        poems.append(poem)
    for poem in poems:
        print(poem)
        print('---' * 80)

    pass

def main():
    for page in range(5):
        print("正在爬取 第 "+str(page)+" 页")
        get_poem(page)

    pass

if __name__ == '__main__':
    main()
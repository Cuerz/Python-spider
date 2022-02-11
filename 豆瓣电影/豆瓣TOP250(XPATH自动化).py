# -*- encoding: UTF-8 -*-
#使用XPATH爬取豆瓣电影TOP250榜单中序号、对应电影、对应电影评分和电影图片地址

import requests
from lxml import etree
# 获取电影信息
def get_film(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    # 网页的源码
    html_doc = response.content.decode("utf-8")
    # 使用etree去转化html_doc，转化为了一个html的对象，此时element对象可以使用xpath语法
    html = etree.HTML(html_doc)
    # 获取电影排名
    number = html.xpath("//div[@class='pic']/em/text()")
    # 获取电影名
    name = html.xpath("//div[@class='hd']/a/span[1]/text()")
    # 获取电影评分
    score = html.xpath("//div[@class='star']/span[2]/text()")
    # 获取图片地址
    pic_url = html.xpath("//div[@class='pic']/a/img/@src")
    # 输出电影排名 电影名 评分 图片地址
    for i in range(25):
        print(number[i] + ' ' + name[i] + ' ' + score[i] + ' ' + pic_url[i])

    pass

# 自动获取下一页地址
def get_nextpage(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    # 网页的源码
    html_doc = response.content.decode("utf-8")
    # 使用etree去转化html_doc，转化为了一个html的对象，此时element对象可以使用xpath语法
    html = etree.HTML(html_doc)
    href = html.xpath("//span[@class='next']/a/@href")
    next_page = "https://movie.douban.com/top250"+href[0]
    return next_page

def main():
    url = "https://movie.douban.com/top250?start=0&filter="
    while True:
        try:
            get_film(url)
            url = get_nextpage(url)
        except:
            break

    pass

if __name__ == '__main__':
    main()
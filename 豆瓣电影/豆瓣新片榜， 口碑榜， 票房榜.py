# -*- encoding: UTF-8 -*-
#使用BeautifulSoup获取豆瓣新片榜， 口碑榜， 票房榜

import requests
from bs4 import BeautifulSoup
#将请求网址定义为get_soup方法，方便二次调用
def get_soup(url):
    url = url
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }
    response = requests.get(url=url,headers=headers)
    # 网页的源码
    html_doc = response.content.decode("utf-8")
    # 使用BeautifulSoup转化源码
    soup = BeautifulSoup(html_doc)
    return soup

def main():
    url = "https://movie.douban.com/chart"
    soup = get_soup(url)

    # 豆瓣新片榜
    print('豆瓣新片排行榜')
    list1 = soup.find('div',class_='article').find_all('table')
    for item1 in list1:
        # 获取电影名
        name = item1.find('a',class_='nbg').get('title')
        # 获取电影评分
        score = item1.find('span',class_='rating_nums').get_text()
        # 获取电影详情页网址，重新请求并获取电影介绍
        href = item1.find('a',class_='nbg').get('href')
        isoup = get_soup(href)
        # 电影简介中有换行情况用replace替换为空
        intro = isoup.find('span',property='v:summary').text.strip().replace(' ','').replace('\n','')
        print('  '+name+'  '+score+'  '+intro)

    # 本周口碑榜
    print('\n本周口碑榜')
    list2 = soup.find_all('div',class_='movie_top')[1].find_all('li',class_='clearfix')
    for item2 in list2:
        # 获取电影排名
        number = item2.find('div').get_text()
        # 获取电影名
        name = item2.find('a').get_text().strip()
        print('  '+number+'  '+name)

    # 北美票房榜
    print('\n北美票房榜')
    list3 = soup.find_all('div',class_='movie_top')[2].find_all('li',class_='clearfix')
    for item3 in list3:
        # 获取电影排名
        number = item3.find('div').get_text()
        # 获取电影名
        name = item3.find('a').get_text().strip()
        # 票房价格
        money = item3.find('span').get_text()
        print('  '+number+'  '+name+'  票房:'+money+'美元')

    pass

if __name__ == '__main__':
    main()

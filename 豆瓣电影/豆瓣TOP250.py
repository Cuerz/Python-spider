# -*- encoding: UTF-8 -*-
#爬取豆瓣电影TOP250榜单中序号、对应电影、对应电影评分和电影图片地址

import requests
from bs4 import BeautifulSoup
def getfilm(page):
    url = "https://movie.douban.com/top250?start={}&filter=".format(page*25)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    html_doc = response.content.decode("utf-8")
    soup = BeautifulSoup(html_doc)
    list = soup.find('ol', class_='grid_view').find_all('li')
    for item in list:
        name = item.find('div', class_='hd').find('span', class_='title').get_text()
        number = item.find('em').get_text()
        score = item.find('div', class_='bd').find('span', class_='rating_num').get_text()
        pic_url = item.find('div', class_='pic').find('img').get('src')
        print(number+' '+name + ' ' + score + ' ' + pic_url)

    pass

def main():
    for i in range(10):
        getfilm(i)

    pass

if __name__ == '__main__':
    main()
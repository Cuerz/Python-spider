# -*- encoding: UTF-8 -*-
#爬取豆瓣电影动作片排行榜

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def get_driver(url):
    options = webdriver.ChromeOptions()
    # 浏览器使用静默模式
    options.add_argument("headless")
    driver = webdriver.Chrome("/爬虫/chromedriver.exe", options=options)
    driver.get(url)
    return driver

def main():
    url="https://www.ygdy8.net/html/gndy/china/list_4_1.html"
    driver = get_driver(url)
    try:
        while driver.find_element_by_xpath("//a[contains(text(),'下一页')]"):
            # 寻找电影详情页链接
            dest = driver.find_elements_by_xpath("//b/a[2]")
            for dst in dest:
                # 点击进入单个电影详情页
                dst.click()
                # 切换选项卡
                driver.switch_to.window(driver.window_handles[1])
                # 获取电影信息
                title = driver.find_element_by_xpath("//h1/font").text
                # 有的电影并没有图片信息
                try:
                    if driver.find_element_by_xpath("//span/img"):
                        pic_url = driver.find_element_by_xpath("//span/img").get_attribute('src')
                    else:
                        pic_url = ''
                except:
                    pass
                print(title + ' ' + pic_url)
                # 关闭单个电影详情页
                driver.close()
                # 切换选项卡到原来的界面
                driver.switch_to.window(driver.window_handles[0])
            # 寻找下一页链接
            driver.find_element_by_xpath("//a[contains(text(),'下一页')]").click()
            # 关闭当前选项卡
            driver.close()
            # 进入下一页
            driver.switch_to.window(driver.window_handles[0])
    except:
        print("end")
    time.sleep(3)
    driver.quit()
    pass

if __name__ == '__main__':
    main()

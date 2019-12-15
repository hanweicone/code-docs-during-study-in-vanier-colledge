"""
爬取豆瓣电影Top250
"""
# -*- coding: utf-8 -*-
import os
import re
import time
import requests
from bs4 import BeautifulSoup
import csv

def download(url, page):
    print(f"正在爬取：{url}")  # f-strings in python 3
    kv = {'user-agent': 'Mozilla/5.0'}  # 不加header跑不起来（必须要伪装成浏览器）
    html = requests.get(url, headers=kv).text   # 这里不加text返回<Response [200]>
    soup = BeautifulSoup(html, 'html.parser')
    lis = soup.select("ol li")
    for li in lis:
        index = li.find('em').text
        title = li.find('span', class_='title').text
        rating = li.find('span', class_='rating_num').text
        strInfo = re.search("(?<=<br/>).*?(?=<)", str(li.select_one(".bd p")), re.S | re.M).group().strip()
        infos = strInfo.split('/')
        year = infos[0].strip()
        area = infos[1].strip()
        type = infos[2].strip()
        write_fo_file(index, title, rating, year, area, type)
    page += 25
    if page < 250:
        time.sleep(2)
        download(f"https://movie.douban.com/top250?start={page}&filter=", page)


def write_fo_file(index, title, rating, year, area, type):
    f = open('movie_top250.csv', 'a', newline='', encoding='utf-8-sig')  # 注意'a' 代表最后row的后面写入，'w'代表覆盖写入,用'utf-8'会有中文乱码
    # csv_writer = csv.writer(f)
    # list = []
    # list.append(index)
    # list.append(title)
    # list.append(rating)
    # list.append(year)
    # list.append(area)
    # list.append(type)
    # csv_writer.writerow(list)
    f.write(f'{index},{title},{rating},{year},{area},{type}\n')#上面代码的简写方法,不需要用到csv
    f.close()


def main():
    if os.path.exists('movie_top250.csv'):
        os.remove('movie_top250.csv')

    url = 'https://movie.douban.com/top250'
    download(url, 0)
    print("爬取完毕。")

if __name__ == '__main__':
    main()







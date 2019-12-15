"""
scrape videos information from youtube
"""
# -*- coding: utf-8 -*-
'''
this code is works for python 3
'''
import os
import requests  # do not know if requests is works on python2
from bs4 import BeautifulSoup
import csv


def download(url):
    print(f"scraping from：{url}")
    kv = {'user-agent': 'Mozilla/5.0'}
    html = requests.get(url, headers=kv).text
    soup = BeautifulSoup(html, 'html.parser')
    imgs = []
    titles = []
    numberofviews = []
    duarations = []

    list = soup.findAll('img', attrs={'width': "196"})
    for x in list:
        imgs.append(x['src'])

    list1 = soup.findAll('a', attrs={
        'class': 'yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2'})
    for x in list1:
        titles.append(x['title'])

    list2 = soup.findAll('span', attrs={'class': 'video-time'})
    for x in list2:
        duarations.append(x.text)

    list3 = soup.findAll('ul', attrs={'class': 'yt-lockup-meta-info'})
    for x in list3:
        numberofviews.append(x.findChildren('li')[0].text)

    f = open('youtube.csv', 'a', newline='', encoding='utf-8-sig')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['title', 'views', 'duaration', 'img url'])
    for i in range(len(titles)):
        csv_writer.writerow([titles[i], numberofviews[i], duarations[i], imgs[i]])
    f.close()


def main():
    if os.path.exists('youtube.csv'):
        os.remove('youtube.csv')
    '''
    url could be uploader's  home page or video page
    '''
    # url = "https://www.youtube.com/channel/UCoC47do520os_4DBMEFGg4A/videos"  # this is video page
    url = "https://www.youtube.com/channel/UCoC47do520os_4DBMEFGg4A/featured"  # this is home page
    download(url)
    print("scraping completed")


if __name__ == '__main__':
    main()

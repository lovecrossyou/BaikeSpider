#coding=utf-8
import urllib
import re
import datetime


def getHtml(url):
    page = urllib.urlopen(url)
    if page.getCode() != 200:
        print('xxxxx');

    html = page.read()
    return html


def getImg(html):
    splitReg = r'[\s\"]+'
    tempList = re.split(splitReg, html)  # 分割后获得一个list （数组）
    imgUrls = []  # 一个空list

    x = 0
    for str in tempList:
        matchReg = r'http:.*.jpg'
        if re.match(matchReg, str):
            print('%s--' % x + str)
            imgUrls.append(str)
            x = x + 1
            # urllib.urlretrieve(str, '%s %s.jpg' % (datetime.datetime.now(), x))
        matchReg1 = r'http:.*.png'
        if re.match(matchReg1, str):
            print('%s--' % x + str)
            imgUrls.append(str)
            x = x + 1
            # urllib.urlretrieve(str, '%s %s.jpg' % (datetime.datetime.now().date(), x))
    return imgUrls

url2 = 'http://cn.bing.com/images/search?q=张鲁一&go=搜索&qs=n&form=QBIR&pq=张鲁一&sc=8-3&sp=-1&sk='
html = getHtml(url2)
print(html)
getImg(html)

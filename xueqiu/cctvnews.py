
# -*- coding: utf-8 -*-
import StringIO
import datetime
import re
import time
import urllib2

from BeautifulSoup import BeautifulSoup, Comment
from docx import Document
from docx.shared import Inches


def downloadTodayNews():
    currentTime = datetime.date.today()
    if datetime.datetime.now().hour <= 19 :
        currentTime = datetime.date.today() - datetime.timedelta(days=1)
    strTime = currentTime.strftime('%Y%m%d')
    url = 'http://cctv.cntv.cn/lm/xinwenlianbo/%s.shtml' %strTime
    soup = BeautifulSoup(getPageContent(url))
    getnewslist = soup.findAll(attrs={"class" : "title2 fs_14"})

    with open(strTime+'.html','w') as f:
        for i in getnewslist:
            for news in i.findAll('li'):
                artileUrl = news.find("a").get("href");
                print artileUrl
                article_soup = BeautifulSoup(getPageContent(artileUrl))
                text = article_soup.find(attrs={"class" : 'body'})
                f.write('<b>'+news.find("a").contents[0].encode('gb2312')+'</b>'+'\n')
                f.write('<div class="body">')
                f.write(text.text.encode("gb2312") + "</div>" + '\n')

def getPageContent(link):
    req_header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept':'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Connection':'close',
    'Referer':None
    }
    try :
        req_timeout=1000
        req=urllib2.Request(link, None, req_header)
        resp=urllib2.urlopen(req, None, req_timeout)
        html = resp.read()
    except Exception,ex:
        html = ""
    html = unicode(html, "utf8")
    return html                
                
if __name__ == '__main__':
    downloadTodayNews()
    print "制作完毕"




# -*- coding: utf-8 -*-
import StringIO
import datetime
import re
import time
import urllib2

from BeautifulSoup import BeautifulSoup, Comment, Tag


def get_all_pages():
    lists = []
    for i in range(1, 6) :
        lists.append("http://blog.csdn.net/v_JULY_v/article/list/%d" %i)
    return lists   

def get_page_articles(page_link):
    req_header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept':'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Connection':'close',
    'Referer':None
    }
    page = BeautifulSoup(getPageContent(page_link, req_header))
    article_spans = page.findAll(attrs={"class" : "link_title"})
    index = 0
    for article_span in article_spans :
        if index == 0 : 
            index = index + 1
            continue
            
        article_link = "http://blog.csdn.net%s" %article_span.a["href"]
        print article_link
        article = BeautifulSoup(getPageContent(article_link, req_header), convertEntities=BeautifulSoup.HTML_ENTITIES)
        title = article.find('h1')
        parags = article.findAll("p")
        print title.text
        for parag  in parags : 
            print parag.text
        break
    
def getPageContent(link, req_header):
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
   lists = get_all_pages()
   get_page_articles(lists[0])

# -*- coding: utf-8 -*-
import urllib2

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
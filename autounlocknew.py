# -*- coding: utf-8 -*-

import requests
import urllib
import re
from BeautifulSoup import BeautifulSoup
import urllib2	
import time
import md5
from cookielib import CookieJar
import chardet

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Autounlock:
    def __init__(self):
        self.session = requests.Session()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CookieJar()))

    def fname(self):
        """docstring for fname"""
        pass

    def get(self, url, data={}):
        return self.request(url, 'get', data)

    def post(self, url, data={}):
        return self.request(url, 'post', data)

    def request(self, url, method, data={}):
        if method == 'get':
            return self.session.get(url, data=data)
        elif method == 'post':
            return self.session.post(url, data=data)
    
    def checkIfUnlock(self):
        result = urllib.urlopen('http://www.baidu.com')
        html = result.read().decode('utf-8')
        soup = BeautifulSoup(html)

        table = soup.findAll("td", align="right")
        newtable = soup.findAll("td", align="center")

        resultlist = [item.text for item in table]
        newresultlist = [item.text for item in newtable]
        
        print '---result---'
        for item in resultlist:
        	print item

        print '---newresult---'
        for item in newresultlist:
            print item

        if '解锁URL:' in resultlist:
            print 'case1 yes'
            #self.postToNic()
            self.nicLogin()
            self.nicStatus()
            self.nicUnlock()
        else:
            print 'case1 no'
        
        if '请按此按钮解锁：' in newresultlist:
            print 'case2 yes'
            self.nicLogin()
            self.nicStatus()
            self.nicUnlock()
        else:
            print 'case2 no'

    def nicLoginUseUrllib(self):
        print 'cleantha'
        data = {
            'error_info': '',
            'username': '213101579',
            'password': '888888'
        }

        url = 'https://nic.seu.edu.cn/selfservice/campus_login.php'
        req = urllib2.Request(url,  urllib.urlencode(data))
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')
        try:
            res = self.opener.open(req)
            html = res.read()
            print type(html)
            print html.decode('gb2312').encode('utf-8')
            # print res.read().decode('gb2312').encode('utf-8')
        except:
            pass

    def nicStatusUseUrllib(self):
        data = {
            'operation': 'status',
            'item': 'web',
            'error_info': '',
            'web_sel': '1'
        }	

        url = 'https://nic.seu.edu.cn/selfservice/service_manage_index.php'
        req = urllib2.Request(url,  urllib.urlencode(data))
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')
        try:
            res = self.opener.open(req)
            # print res.read().decode('gb2312').encode('utf-8')
        except:
            pass

    def nicUnlockUseUrllib(self):
        data = {
            'operation': 'unlock',
            'item': 'web',
            'error_info': '',
            'kick_ip_address': '',
            'session_id': '',
            'nas_ip_address': ''
        }

        url = 'https://nic.seu.edu.cn/selfservice/service_manage_status_web.php'
        req = urllib2.Request(url,  urllib.urlencode(data))
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')
        try:
            res = self.opener.open(req)
            # print res.read().decode('gb2312').encode('utf-8')
        except:
            pass


    def nicLogin(self):
        data = {
            'error_info': '',
            'username': '213101579',
            'password': '888888'
        }

        url = 'https://nic.seu.edu.cn/selfservice/campus_login.php'

        response = self.post(url, data)
        print response.encoding
        #response.encoding = 'gbk'
        response.encoding = 'gb2312'
        print response.text
        #print self.post(url, data).text
        # print requests.utils.get_unicode_from_response(self.post(url, data))
        # print str(self.post(url, data).text).decode('gb2312').encode('utf-8')
        #print type(self.session.cookies)
        # print dict(self.session)
        #self.saveCookie()

    def nicStatus(self):
        data = {
            'operation': 'status',
            'item': 'web',
            'error_info': '',
            'web_sel': '1'
        }	

        url = 'https://nic.seu.edu.cn/selfservice/service_manage_index.php'

        response = self.post(url, data)
        print response.encoding
        #response.encoding = 'gbk'
        response.encoding = 'gb2312'
        print response.text
        #print self.post(url, data).text.decode('utf-8')
        #print type(self.session.cookies)

        #for cookie in self.session.cookies:
        #	print cookie
        # print dict(self.session)

    def nicUnlock(self):
        data = {
            'operation': 'unlock',
            'item': 'web',
            'error_info': '',
            'kick_ip_address': '',
            'session_id': '',
            'nas_ip_address': ''
        }

        url = 'https://nic.seu.edu.cn/selfservice/service_manage_status_web.php'
        response = self.post(url, data)
        print response.encoding
        response.encoding = 'gbk'
        print response.text
        #print self.post(url, data).text.decode('utf-8')

if __name__ == '__main__':
    autounlock = Autounlock()
    while True:
        autounlock.checkIfUnlock()
        time.sleep(3)

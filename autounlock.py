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

    def get(self, url, data={}):
        return self.request(url, 'get', data)

    def post(self, url, data={}):
        return self.request(url, 'post', data)

    def request(self, url, method, data={}):
        # if data:
        #     data.update(self.token)

        if method == 'get':
            return self.session.get(url, data=data)
        elif method == 'post':
            return self.session.post(url, data=data)

    def postToNic(self):
        data = {
            'operation' : 'status',
            'item' : 'web',
            'error_info' : '',
            'web_sel' : 1
        }
        req = urllib2.Request("https://nic.seu.edu.cn/selfservice/service_manage_index.php", urllib.urlencode(data))
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')
        try:
            res = urllib2.urlopen(req, timeout=8)
            print res.read()
        except urllib2.HTTPError:
            print 'nic server error'

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

    def testencode(self):
        print self.get("http://www.baidu.com").text

    def nicDecryption(self, ciphertext=''):
        ciphertext = '508986be165780ff2eaa5bf465d1ff3e'
        for i in xrange(1000000000):
            newciphertext = md5.new(str(i)).hexdigest()
            if newciphertext == ciphertext:
                print 'the password is' + str(i) 
                break

    def nicEncryption(self):
        origintext = '333333'
        ciphertext = md5.new(origintext).hexdigest()
        print ciphertext
        print type(ciphertext)
        print len(ciphertext)

    def nicLoginUseUrllibNew(self):
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CookieJar()))
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
            res = opener.open(req)
            html = res.read()
            print type(html)
            print html.decode('gb2312').encode('utf-8')
            # print res.read().decode('gb2312').encode('utf-8')
        except:
            pass

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

    def nicLoginNew(self):
        data = {
            'error_info': '',
            'username': '213101579',
            'password': '888888'
        }

        url = 'https://nic.seu.edu.cn/selfservice/campus_login.php'
        response = requests.Session().post(url, data=data)
        print response.encoding	
        # response.encoding = 'gb2312'
        html = response.text
        print requests.utils.get_encodings_from_content(html)

        # html = response.content.decode('gb2312').encode('utf-8')
        # print html
        #print chardet.detect(html)
        #print typezz(html)
        # print html
        # print response.text.encode('gb2312')

    def nicLogin(self):
        data = {
            'error_info': '',
            'username': '213101579',
            'password': '888888'
        }

        url = 'https://nic.seu.edu.cn/selfservice/campus_login.php'

        response = self.post(url, data)
        print response.encoding
        response.encoding = 'gbk' #gb2312 is ok
        #print response.text
        print 'niclogin'
        #print self.post(url, data).text
        # print requests.utils.get_unicode_from_response(self.post(url, data))
        # print str(self.post(url, data).text).decode('gb2312').encode('utf-8')
        #print type(self.session.cookies)
        # print dict(self.session)
        #self.saveCookie()

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
        response.encoding = 'gbk' #gb2312 is ok
        #print response.text
        print 'nicUnlock'
        #print self.post(url, data).text.decode('utf-8')

    def saveCookie(self):
        cookie_dict = requests.utils.dict_from_cookiejar(self.session.cookies)
        cookie_str = '; '.join([k + '=' + v for k, v in cookie_dict.iteritems()])
        print '-----------------'
        print cookie_str
        print '-----------------'

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
        response.encoding = 'gbk' #gb2312 is ok
        #print response.text
        print 'nicstatus'
        #print self.post(url, data).text.decode('utf-8')
        #print type(self.session.cookies)

        #for cookie in self.session.cookies:
        #	print cookie
        # print dict(self.session)

    def testredirect(self):
        data = {
            'name' : 'cleantha'
        }

        req = urllib2.Request("http://127.0.0.1:8000/aaahehe/", urllib.urlencode(data))
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0')
        try:
            res = urllib2.urlopen(req, timeout=8)
            print res.read()
        except urllib2.HTTPError:
            print 'nic server error'

if __name__ == '__main__':
    autounlock = Autounlock()
    # autounlock.checkIfUnlock()
    # while True:
    #         autounlock.testredirect()
    # 	print autounlock.post('http://127.0.0.1:8000/aaahehe/', {'name': 'clea'}).text
    # 	time.sleep(3)
    #print '-----------------------'
    #autounlock.nicLogin()
    #print '-----------------------'
    #autounlock.nicStatus()
    #print '-----------------------'
    #autounlock.nicUnlock()
    #print '-----------------------'
    autounlock.checkIfUnlock()
    #autounlock.nicLoginNew()
    #autounlock.testencode()
    # autounlock.nicDecryption()
    #autounlock.nicEncryption()
    #autounlock.nicLoginUseUrllib()
    # print '----------------------'
    # autounlock.nicLoginUseUrllib()
    # print '----------------------'
    # autounlock.nicStatusUseUrllib()
    # print '----------------------'
    # autounlock.nicUnlockUseUrllib()
    # print '----------------------'
    #autounlock.nicLoginNew()
    # autounlock.nicLoginUseUrllibNew()


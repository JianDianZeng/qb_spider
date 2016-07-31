#coding:utf-8
from bs4 import BeautifulSoup
import urllib2
import re
import time
page = 1
datas=[]
while page<10:
    try:
        print '爬取第'+str(page)+"页中："
        time.sleep(1)
        url="http://www.qiushibaike.com/8hr/page/"+str(page)
        request = urllib2.Request(url)
        request.add_header("user-agent","Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)")
        response = urllib2.urlopen(request)
        data= response.read()
        soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
        res = soup.find_all("img", src= re.compile(r"http://pic.qiushibaike.com/system/avtnew/\d+/\d+/medium/\d+\.jpg"))
        datas.append(res)
        page=page+1
        print 'success'
    except:
        print 'fail'

fout =open('pic.html', 'w')
for data in datas:
    fout.write("%s" %data)

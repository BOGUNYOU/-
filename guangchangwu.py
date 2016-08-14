#_*_ coding:utf-8_*_
import re
import urllib2
import urllib
import cookielib
import socket
import time
socket.setdefaulttimeout(20)
url = 'http://www.cntaijiquan.com/gcw/10175.html'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Cache-Control':'max-age=0'
	}
cookie = cookielib.CookieJar()
handle = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handle)
request = urllib2.Request(url = url,headers = headers)
response = urllib2.urlopen(request)
contents = response.read()
mattern = r'(http://flv[^"]+)'
mattern2 = r'flv">([^<]+)'
song_name = re.compile(mattern2).findall(contents)
songs_url = re.compile(mattern).findall(contents)
all_song_name = []
all_song_url = []
for i in song_name:
    single_song_name =  i.decode('utf-8').encode('gbk')+".flv"
    all_song_name.append(single_song_name)
for i in songs_url:
    single_song_url =  i.decode('utf-8').encode('gbk')
    all_song_url.append(single_song_url)
def Schedule(a,b,c):
    per = 100.0 * a * b/c
    if per >100:
        per = 100
    print '%.2f%%' % per
for i in range(all_song_url.__len__()):
    try:
        urllib.urlretrieve(all_song_url[i],filename=all_song_name[i],reporthook=Schedule)
        print all_song_name[i]+"已下载"
        time.sleep(100)
    except:
        urllib.urlretrieve(all_song_url[i], filename=all_song_name[i], reporthook=Schedule)
        print all_song_name[i] + "已下载"
        pass

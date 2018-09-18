import multiprocessing
import time
start=time.time()
import os
import urllib2
from urlgrabber.keepalive import HTTPHandler
from bs4 import BeautifulSoup
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',																																																																																																																																																																																																																							
       'Connection': 'keep-alive'}
def gsearch(an1):
	quoted_query = urllib2.quote(an1)
	quote_page ="https://www.google.co.in/search?q=" +quoted_query+ "&oq="+quoted_query+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
	req = urllib2.Request(quote_page, headers=hdr)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page, 'html.parser')
	name_box2= soup.find('div', attrs={'class': 'ab_tnav_wrp'})
	name2 = name_box2.text.strip()
	name2=name2.split(' ')
	name3=name2[1].replace(',','')
	a1rcount=(name3)
	print a1rcount
	abc=open("maina1.txt","w")
	abc.write(a1rcount)
	abc.close()
keepalive_handler = HTTPHandler()
opener = urllib2.build_opener(keepalive_handler)
urllib2.install_opener(opener)

abbc=open("main.txt","r")
lis=abbc.readlines()
for i in lis:
	j=i.split(" ")
	if j[0]=="a1":
		a1=i[3:len(i)+1]
	elif j[0]=="q":
		q=i[2:len(i)+1]
a1=a1.replace(" ","+")
query=q+' '+'+'+a1
abbc.close()
pool = multiprocessing.Pool(processes=10)
for i in range(6):
	pool.map(gsearch,[query,query,q,a1])
end=time.time()
abc=end-start
print abc

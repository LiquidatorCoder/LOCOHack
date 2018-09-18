import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
#import mechanize
import os
import urllib2
#from bs4 import BeautifulSoup
#import time
from webbrowser import *
#from google import google
num_page = 3
"""
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv( True ) 
br.set_handle_gzip( True ) 
br.set_handle_redirect( True ) 
br.set_handle_referer( True )
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]"""
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',																																																																																																																																																																																																																							
       'Connection': 'keep-alive'}



while True:
    a=raw_input("===")
    os.system("adb shell screencap -p /sdcard/new.jpg")
    os.system("adb pull /sdcard/new.jpg")
    
    
    img =Image.open('new.jpg')
    w = img.size[0]
    h = img.size[1]
    p=30
    a=img.crop((p,500,w-p,h-1160))
    a.save('ques.jpg')
    ques = (pytesseract.image_to_string(Image.open('ques.jpg'),lang='eng')).lower()
    print ques
    """resp0=br.open("https://www.google.co.in")
    br.select_form('f')
    br.form['q']='site:quora.com '+ques
    br.submit()
    resp = None
    x=0
    for link in br.links():
        if '/search' not in link.url:
            if 'quora.com' in link.url:
           	if '/url?q=' in link.url:
    		    ur=link.url
	            x+=1
		    urr=ur.split('/url?q=')
		    urrr=urr[1]
		    urrrr=urrr.split('&sa')
		    lin=urrrr[0]
		    break
	else:
	    lin=None
    count=0
    ques1=ques.split(' ')
    if lin!=None:
	for i in ques1:
            if i in lin:
	        count+=1
            else:
                count-=1"""
    count=0
    if count>0:
        open_new(lin)
    else:
        new2=1
        
        
        
    if new2==1:
        que=''
        quues=ques.split('\n')
        for kw in quues:
            que+=kw+' '
        quoted_query = urllib2.quote(que.encode('utf8'))
        quote_page ="https://www.google.co.in/search?q=" +quoted_query+ "&oq="+quoted_query+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
	open_new(quote_page)
	

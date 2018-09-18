import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import requests,mechanize
import os
import urllib2
from bs4 import BeautifulSoup
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv( True ) 
br.set_handle_gzip( True ) 
br.set_handle_redirect( True ) 
br.set_handle_referer( True )
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',																																																																																																																																																																																																																							
       'Connection': 'keep-alive'}
while True:
    a=raw_input(":")
    """
    os.system("adb devices")
    os.system("adb shell screencap -p /sdcard/new.png")
    os.system("adb pull /sdcard/new.png new.png")
    """
    img =Image.open('new.png')
    w = img.size[0]
    h = img.size[1]
    p=30
    a=img.crop((p,700,w-p,h-960))
    b=img.crop((p+120,h-990,w-p-120,h-810))
    c=img.crop((p+120,h-840,w-p-120,h-630))
    d=img.crop((p+120,h-660,w-p-120,h-450))
    a.save('ques.png')
    b.save('ans1.png')
    c.save('ans2.png')
    d.save('ans3.png')
    ques = (pytesseract.image_to_string(Image.open('ques.png'),lang='eng')).lower()
    aans1 = (pytesseract.image_to_string(Image.open('ans1.png'),lang='eng')).lower()
    aans2 = (pytesseract.image_to_string(Image.open('ans2.png'),lang='eng')).lower()
    aans3 = (pytesseract.image_to_string(Image.open('ans3.png'),lang='eng')).lower()

    """
    
    ques=raw_input('Q:')
    ans1=raw_input('A1:')
    ans2=raw_input('A2:')
    ans3=raw_input('A3:')
    """
    ans1=aans1.split(' ')
    ans2=aans2.split(' ')
    ans3=aans3.split(' ')
    print ques
    print aans1,aans2,aans3
    resp0=br.open("https://www.google.co.in")
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
    count=0
    ques1=ques.split(' ')
    for i in ques1:
        if i in lin:
	    count+=1
        else:
            count-=1
    if count>0:
        print lin
        resp1=br.open(lin)
        sclist=[]
        for link in br.links():
            b=link.text.lower()
            a=b.split()
            sclist.extend(a)
        nstr=''
        for i in sclist:
            nstr+=i

        d1=0
        d2=0
        d3=0
        for i in ans1:
            ansl1=nstr.split(i)
            d1+=len(ansl1)
        for i in ans2:
            ansl2=nstr.split(i)
            d2+=len(ansl2)
        for i in ans3:
            ansl3=nstr.split(i)
            d3+=len(ansl3)
        new2=max(d1,d2,d3)
    else:
        new2=1
    if new2==1:
        que=''
        quues=ques.split('\n')
        for kw in quues:
            que+=kw+' '
        quoted_query = urllib2.quote(que.encode('utf8'))
        quote_page ="https://www.google.co.in/search?q=" +quoted_query+ "&oq="+quoted_query+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
        req = urllib2.Request(quote_page, headers=hdr)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page, 'html.parser')
        try:
            name_box2= soup.find('div', attrs={'class': 'vk_bk vk_ans'})
            name2 = name_box2.text.strip()
            print name2
        except:
            try:
	        name_box = soup.find('div', attrs={'class': '_XWk'})
                name = name_box.text.strip()
                print name
            except:
                try:
       	            name_box3 = soup.find('div', attrs={'class': '_wjf'})
	            name3 = name_box3.text.strip()
	            print name3
	        except:
	            try:
			#raise IOError
       	                name_box4 = soup.find('span', attrs={'class': '_Tgc _s8w'})
		        for b_tag in soup.find_all('b'):
		            print b_tag.text
	            except:
    			ques2=""
    			for j in ques1:
        		    if j not in ['how','who','what','which','when','is','where','are','many','have','has','of']:
	    			ques2=ques2+j+' '
	                resp2=br.open("https://www.google.com")
		        br.select_form('f')
  		        br.form['q']=ques2
    		        br.submit()
    		        resp = None
    		        sclist2=[]
   		        nstr2=''
    		        for lin in br.links():
	                    b=lin.text.lower()
                            a=b.split()
        		    sclist2.extend(a)
    		        for i in sclist2:
        		    nstr2+=i
    		        print ques2
    		        c1=nstr2.split(aans1)
    		        c2=nstr2.split(aans2)
    		        c3=nstr2.split(aans3)
    		        new3=max(len(c1),len(c2),len(c3))

    		        if new3==1:
        		        print "Can't Find"
    		        elif new3==len(c1):
        		        print aans1
    		        elif new3==len(c2):
        		        print aans2
    		        elif new3==len(c3):
        		        print aans3

    elif new2==d1:
        print aans1
    elif new2==d2:
        print aans2
    elif new2==d3:
        print aans3

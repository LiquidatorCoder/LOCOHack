import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import requests,mechanize
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv( True ) 
br.set_handle_gzip( True ) 
br.set_handle_redirect( True ) 
br.set_handle_referer( True )
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

"""
ques = (pytesseract.image_to_string(Image.open('ques.jpg'),lang='eng')).lower()
ans1 = (pytesseract.image_to_string(Image.open('ans1.jpg'),lang='eng')).lower()
ans2 = (pytesseract.image_to_string(Image.open('ans2.jpg'),lang='eng')).lower()
ans3 = (pytesseract.image_to_string(Image.open('ans3.jpg'),lang='eng')).lower()
"""
ques=raw_input('Q:')
ans1=raw_input('A1:')
ans2=raw_input('A2:')
ans3=raw_input('A3:')
ans1=ans1.replace(' ','')
ans2=ans2.replace(' ','')
ans3=ans3.replace(' ','')
print ques
print ans1,ans2,ans3
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
print sclist


ansl1=nstr.split(ans1)
ansl2=nstr.split(ans2)
ansl3=nstr.split(ans3)
new2=max(len(ansl1),len(ansl2),len(ansl3))
print len(ansl1),len(ansl2),len(ansl3)
if new2==1:
    print"Google"
    resp2=br.open("https://www.google.com")
    br.select_form('f')
    br.form['q']=ques
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
    print sclist2
    c1=nstr2.split(ans1)
    c2=nstr2.split(ans2)
    c3=nstr2.split(ans3)
    new3=max(len(c1),len(c2),len(c3))
    if new3==1:
        print "Can't Find"
    elif new3==len(c1):
        print ans1
    elif new3==len(c2):
        print ans2
    elif new3==len(c3):
        print ans3
elif new2==len(ansl1):
    print "Quora",ans1
elif new2==len(ansl2):
    print "Quora",ans2
elif new2==len(ansl3):
    print "Quora",ans3

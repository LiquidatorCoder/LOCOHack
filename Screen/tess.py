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
#im = Image.open("desk1.jpg") # the second one 
"""im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.jpg')

"""
ques=raw_input('Q:')
ans1=raw_input('A1:')
ans2=raw_input('A2:')
ans3=raw_input('A3:')
resp0=br.open("https://google.com")
ans1=ans1.replace(' ','')
ans2=ans2.replace(' ','')
ans3=ans3.replace(' ','')
print ques
print ans1,ans2,ans3
br.select_form('f')
br.form['q']='site:quora.com '+ques      #'who co-founded microsoft with allen paul'
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
c1=0
c2=0
c3=0
"""
ans1='jeff'
ans2='bill'
ans3='clinton'

for i in sclist:
    if i==ans1:
        c1+=1
    elif i==ans2:
        c2+=1
    elif i==ans3:
        c3+=1
"""
ansl1=nstr.split(ans1)
ansl2=nstr.split(ans2)
ansl3=nstr.split(ans3)
new2=max(len(ansl1),len(ansl2),len(ansl3))
new=max(c1,c2,c3)
if new2==len(ansl1):
    print ans1
elif new2==len(ansl2):
    print ans2
elif new2==len(ansl3):
    print ans3

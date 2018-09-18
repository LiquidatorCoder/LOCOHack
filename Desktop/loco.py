import pytesseract
from PIL import Image
import urllib2
from webbrowser import open_new
from google import google
from os import system
from collections import Counter
import time
num_page = 2
w = 1080
h = 1920
p=int(0.027777778*w)
h1=int(0.36458333333*h)
h2=int(0.5*h)
h3=int(0.484375*h)
h4=int(0.578125*h)
h5=int(0.5825*h)
h6=int(0.681875*h)
h7=int(0.67625*h)
h8=int(0.775625*h)
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',																																																																																																																																																																																																																							
       'Connection': 'keep-alive'}



while True:
    a=raw_input("===")
    start = time.time()
    system("adb shell screencap -p /sdcard/new.jpg")
    system("adb pull /sdcard/new.jpg")
    img =Image.open('new.jpg')
    a=img.crop((p,h1,w-p,h2))
    a.save('ques.jpg')
    ques = (pytesseract.image_to_string(Image.open('ques.jpg'),lang='eng')).lower()
    print ques
    quues=ques.split('\n')
    que=''
    for i in quues:
        que+=i+' '
    b=img.crop((5*p,h3,w-(5*p),h4))
    b.save('ans1.jpg')
    del b
    c=img.crop((5*p,h5,w-(5*p),h6))
    c.save('ans2.jpg')
    del c
    d=img.crop((5*p,h7,w-(5*p),h8))
    d.save('ans3.jpg')
    del d
    aans1 = (pytesseract.image_to_string(Image.open('ans1.jpg'),lang='eng')).lower()
    aans2 = (pytesseract.image_to_string(Image.open('ans2.jpg'),lang='eng')).lower()
    aans3 = (pytesseract.image_to_string(Image.open('ans3.jpg'),lang='eng')).lower()
    ans1=aans1.split(' ')
    ans2=aans2.split(' ')
    ans3=aans3.split(' ')
    search_results = google.search(que, num_page)
    liss=[]
    lis1=[]
    lis2=[]
    kw=['how','who','what','which','when','is','where','are','many','have','has','of','the','an','a',' of ',' of','of ']
    a1=0
    a2=0
    a3=0
    for result in search_results:
        lis1=result.name.lower().split(' ')
        lis2=result.description.lower().split(' ')
        liss.extend(lis1)
        liss.extend(lis2)
    jq=Counter(liss)
    for i in ans1:
        try:
	    if i not in kw:
	        a1+=jq[i]
	except:
	    pass
    for i in ans2:
        try:
	    if i not in kw:
	        a2+=jq[i]
	except:
	    pass
    for i in ans3:
        try:
	    if i not in kw:
	        a3+=jq[i]
	except:
	    pass
    print a1,a2,a3
    new2=max(a1,a2,a3)
    if new2==0:
        print "No ans"
        end = time.time()
        print"Time Elapsed :",(end - start)
        continue
    elif new2==a1:
        print aans1
	system('adb shell input tap 438 1011')
	system('adb shell input tap 438 1011')
    elif new2==a2:
        print aans2
        system('adb shell input tap 438 1192')
        system('adb shell input tap 438 1192')
    elif new2==a3:
        print aans3
	system('adb shell input tap 438 1383')
	system('adb shell input tap 438 1383')
    end = time.time()
    print"Time Elapsed :",(end - start)

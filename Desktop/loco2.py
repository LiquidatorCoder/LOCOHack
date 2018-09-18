import time,os,webbrowser,collections
from google import google
from PIL import Image
import pytesseract

def screenshot():
	os.system("adb shell screencap -p /sdcard/new.jpg")
	os.system("adb pull /sdcard/new.jpg")
	img=Image.open('new.jpg')
	a_=img.crop([int(q_[0]),int(q_[1]),int(q_[0])+int(q_[2]),int(q_[1])+int(q_[3])])
	b_=img.crop([int(t[0]),int(t[1]),int(t[0])+int(t[2]),int(t[1])+int(t[3])])
	c_=img.crop([int(e[0]),int(e[1]),int(e[0])+int(e[2]),int(e[1])+int(e[3])])
	d_=img.crop([int(r[0]),int(r[1]),int(r[0])+int(r[2]),int(r[1])+int(r[3])])
	a_.save("ques.jpg")
	b_.save("ans1.jpg")
	c_.save("ans2.jpg")
	d_.save("ans3.jpg")
def ocr():
	ques = (pytesseract.image_to_string(Image.open('ques.jpg'),lang='eng')).lower()
	aans1 = (pytesseract.image_to_string(Image.open('ans1.jpg'),lang='eng')).lower()
	aans2 = (pytesseract.image_to_string(Image.open('ans2.jpg'),lang='eng')).lower()
	aans3 = (pytesseract.image_to_string(Image.open('ans3.jpg'),lang='eng')).lower()
	ques=ques.replace('\n',' ')
	lis=[ques,aans1,aans2,aans3]
	return lis
def gsearch(query,num_page,anss1,anss2,anss3):
	search_results = google.search(query, num_page)
	for result in search_results:
        	lis1=result.name.lower().split(' ')
        	lis2=result.description.lower().split(' ')
        	liss.extend(lis1)
        	liss.extend(lis2)
	aann1=anss1.split(' ')
	aann2=anss2.split(' ')
	aann3=anss3.split(' ')
	aa1=counte(liss,aann1)
	aa2=counte(liss,aann2)
	aa3=counte(liss,aann3)
	return aa1,aa2,aa3
def counte(lists,answer):
	jq=collections.Counter(lists)
	a=0
	for i in answer:
		if i not in KW:
	        	a+=jq[i]
	return a
def anscheck(question,answer1,answer2,answer3,ab1,ab2,ab3):
	if ab1==max(ab1,ab2,ab3) and max(ab1,ab2,ab3)!=0 and (ab1!=ab2  and ab1!=ab3):
		print answer1
	elif ab2==max(ab1,ab2,ab3) and max(ab1,ab2,ab3)!=0 and (ab2!=ab1  and ab2!=ab3):
		print answer2
	elif ab3==max(ab1,ab2,ab3) and max(ab1,ab2,ab3)!=0 and (ab3!=ab1  and ab3!=ab2):
		print answer3
	else:
		print "No answer!"
		url ="https://www.google.co.in/search?q=" +question+ "&oq="+question+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
		webbrowser.open_new(url)
	
os.system("adb shell screencap -p /sdcard/test.jpg")
os.system("adb pull /sdcard/test.jpg")
AA=Image.open('test.jpg')
w=AA.size[0]
h=AA.size[1]
p=int(0.027777778*w)
h1=int(0.36458333333*h)
h2=int(0.5*h)
h3=int(0.484375*h)
h4=int(0.578125*h)
h5=int(0.5825*h)
h6=int(0.681875*h)
h7=int(0.67625*h)
h8=int(0.775625*h)
quescoo=str(2*p)+' '+str(h1)+' '+str(980)+' '+str(261)
ans1coo=str(5*p)+' '+str(h3)+' '+str(760)+' '+str(180)
ans2coo=str(5*p)+' '+str(h5)+' '+str(760)+' '+str(180)
ans3coo=str(5*p)+' '+str(h7)+' '+str(760)+' '+str(180)
q_=quescoo.split(' ')
t=ans1coo.split(' ')
e=ans2coo.split(' ')
r=ans3coo.split(' ')


while True:
	KW=['how','who','what','which','when','is','where','are','many','have','has','of','the','an','a']
	num_page=2
	q=[]
	a1=''
	a2=''
	a3=''
	lis1=[]
	lis2=[]
	liss=[]
	x=raw_input("===")
	start=time.time()
	screenshot()
	lis=ocr()
	aa1,aa2,aa3=gsearch(lis[0],num_page,lis[1],lis[2],lis[3])
	print lis[0]
	print aa1,aa2,aa3
	anscheck(lis[0],lis[1],lis[2],lis[3],aa1,aa2,aa3)
	end=time.time()
	print "Time Elapsed : ",end-start



"""

fr=open('new.uzn','w+')
fr.write(quescoo+' '+'Text/Latin'+'\n')
fr.write(ans1coo+' '+'Text/Latin'+'\n')
fr.write(ans2coo+' '+'Text/Latin'+'\n')
fr.write(ans3coo+' '+'Text/Latin')
fr.close()

	os.system('tesseract -l eng -psm 4 new.jpg output')
	fa=open('output.txt','r+')
	a=fa.readlines()
	a=[s.replace("\n","") for s in a]
	a1=''
	a2=''
	a3=''
	for i in range(len(a)):
		if a[i]=='':
			for j in range(0,i):
				if a[j]!="":
					q.append(a[j])
			a1=(a[i+1]).lower()
			a2=(a[i+3]).lower()
			a3=(a[i+5]).lower()
			break
	query=''	
	for i in q:
		query+=i.lower()+' '
"""

"""
w=1080
h=1920
p=int(0.027777778*w)
h1=int(0.36458333333*h)
h2=int(0.5*h)
h3=int(0.484375*h)
h4=int(0.578125*h)
h5=int(0.5825*h)
h6=int(0.681875*h)
h7=int(0.67625*h)
h8=int(0.775625*h)
quescoo=str(p)+' '+str(h1)+' '+str(w-(5*p))+' '+str(h2)
ans1coo=str(5*p)+' '+str(h3)+' '+str(w-(5*p))+' '+str(h4)
ans2coo=str(5*p)+' '+str(h5)+' '+str(w-(5*p))+' '+str(h6)
ans3coo=str(5*p)+' '+str(h7)+' '+str(w-(5*p))+' '+str(h8)
fr=open('new.uzn','w+')
fr.write(quescoo+' '+'Text/Latin'+'\n')
fr.write(ans1coo+' '+'Text/Latin'+'\n')
fr.write(ans2coo+' '+'Text/Latin'+'\n')
fr.write(ans3coo+' '+'Text/Latin')
fr.close()"""
fa=open('output.txt','r+')
a=fa.readlines()
print a
a=[s.replace("\n","") for s in a]
q=[]
a1=[]
a2=[]
a3=[]
for i in range(len(a)):
	if a[i]=='':
		for j in range(0,i):
			if a[j]!="":
				q.append(a[j])
		a1.append(a[i+1])
		a2.append(a[i+3])
		a3.append(a[i+5])
		break
print q
print a1,a2,a3


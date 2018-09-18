import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
img =Image.open('Screenshot_20180226-133801.png')
w = img.size[0]
h = img.size[1]
p=30
a=img.crop((p,700,w-p,h-960))
b=img.crop((p+120,h-990,w-p-120,h-810))
c=img.crop((p+120,h-840,w-p-120,h-630))
d=img.crop((p+120,h-660,w-p-120,h-450))
a.save('temp2.png')
b.save('temp3.png')
c.save('temp4.png')
d.save('temp5.png')
ques = (pytesseract.image_to_string(Image.open('temp2.png'),lang='eng')).lower()
ans1 = (pytesseract.image_to_string(Image.open('temp3.png'),lang='eng')).lower()
ans2 = (pytesseract.image_to_string(Image.open('temp4.png'),lang='eng')).lower()
ans3 = (pytesseract.image_to_string(Image.open('temp5.png'),lang='eng')).lower()
print ques
print ans1
print ans2
print ans3

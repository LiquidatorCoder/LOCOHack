import requests
from urlgrabber.keepalive import HTTPHandler
from bs4 import BeautifulSoup
head = {
    'Host' : 'e-com.secure.force.com',
    'Connection' : 'keep-alive',
    'Upgrade-Insecure-Requests' : '1',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64)',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip, deflate, sdch',
    'Accept-Language' : 'en-US,en;q=0.8'}
url = "https://www.google.co.in/search?dcr=0&source=hp&ei=YrOzWrCpLsHkvATF8bTYDw&q=who+are+you%3F&oq=who+are+you%3F&gs_l=psy-ab.3...5387.9363.0.10148.13.6.0.0.0.0.0.0..0.0....0...1.1.64.psy-ab..13.0.0.0...0.VfGJdBVsohs"
page = requests.get(url,headers=head)
page = page.text
soup = BeautifulSoup(page, 'html.parser')
name_box2= soup.find('div', attrs={'class': 'ab_tnav_wrp'})
name2 = name_box2.text.strip()
name2=name2.split(' ')
name3=name2[1].replace(',','')
a1rcount=(name3)
print a1rcount

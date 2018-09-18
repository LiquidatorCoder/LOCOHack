import urllib2
from bs4 import BeautifulSoup
S=raw_input("Q:")
quoted_query = urllib2.quote(S)
quote_page ="https://www.google.co.in/search?q=" +quoted_query+ "&oq="+quoted_query+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
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
       	        name_box4 = soup.find('span', attrs={'class': '_Tgc _s8w'})
		for b_tag in soup.find_all('b'):
		    print b_tag.text
	    except:
	        print "Can't Find"

from googleapiclient.discovery import build
import pprint,re
from collections import Counter

my_api_key = " AIzaSyDyg1V8OfPJ3ZROn5B_i59LqX0rjH7qr28 "
my_cse_id = "000290359564609275851:vexibvg8nfo"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'who is the first miss world from india', my_api_key, my_cse_id, num=10)
a=[]
for result in results:
    a.append(result['htmlSnippet'])
rd=''
for i in a:
    rd+=i
rs=re.findall(r"[\w']+", rd)
print Counter(rs)

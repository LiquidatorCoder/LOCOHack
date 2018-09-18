from twisted.internet import defer, reactor
from twisted.web.client import getPage
import time

def processPage(page, url):
    # do somewthing here.
    return url, len(page)

def printResults(result):
    for success, value in result:
        if success:
            print 'Success:', value
        else:
            print 'Failure:', value.getErrorMessage()

def printDelta(_, start):
    delta = time.time() - start
    print 'ran in %0.3fs' % (delta,)
    return delta
abbc=open("main.txt","r")
lis=abbc.readlines()
for i in lis:
	j=i.split(" ")
	if j[0]=="a1":
		a1=i[3:len(i)+1]
	elif j[0]=="q":
		q=i[2:len(i)+1]
a1=a1.replace(" ","+")
query=q+' '+'+'+a1
abbc.close()
urls = ['https://www.google.co.in/search?q=who+are+you%3F&gws_rd=cr&dcr=0&ei=Ta2zWuKOA8r7vATpxYiYAg','https://www.google.co.in/search?q=who+are+you%3F&gws_rd=cr&dcr=0&ei=Ta2zWuKOA8r7vATpxYiYAg','https://www.google.co.in/search?q=who+are+you%3F&gws_rd=cr&dcr=0&ei=Ta2zWuKOA8r7vATpxYiYAg','https://www.google.co.in/search?q=who+are+you%3F&gws_rd=cr&dcr=0&ei=Ta2zWuKOA8r7vATpxYiYAg']

def fetchURLs():
    callbacks = []
    for url in urls:
        d = getPage(url)
        d.addCallback(processPage, url)
        callbacks.append(d)

    callbacks = defer.DeferredList(callbacks)
    callbacks.addCallback(printResults)
    return callbacks

@defer.inlineCallbacks
def main():
    times = []
    for x in xrange(5):
        d = fetchURLs()
        d.addCallback(printDelta, time.time())
        times.append((yield d))
    print 'avg time: %0.3fs' % (sum(times) / len(times),)

reactor.callWhenRunning(main)
reactor.run()

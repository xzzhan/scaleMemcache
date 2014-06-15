#!/usr/bin/python
import os, sys, getopt
import string, urllib2
import random

def get_page(page_id,i):
    url0 = 'http://128.148.16.163/wiki/?curid=' + `page_id[0]`
    url1 = 'http://128.148.16.167/wiki/?curid=' + `page_id[1]`
    url2 = 'http://128.148.16.179/wiki/?curid=' + `page_id[2]`
#    print url1
    
    start = os.times()[4]
    response0 = urllib2.urlopen(url0).read()
    elapsed0 = (os.times()[4] - start)
    
    start = os.times()[4]
    response1 = urllib2.urlopen(url1).read()
    elapsed1 = (os.times()[4] - start)
    
    start = os.times()[4]
    response2 = urllib2.urlopen(url2).read()
    elapsed2 = (os.times()[4] - start)

    delay = (elapsed0 + elapsed1 + elapsed2)/3
    #delay = (elapsed1 + elapsed2)/3

    f = open('delay'+str(i)+'.txt', 'a')
    f.write(str(delay)+'\n')
    f.closed

def main(argv):

    i = 0

    try:
        opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
        print 'request generator \n -i <the number>\n'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'request generator \n -i <the number>\n'
            sys.exit()
        elif opt == '-i':
            i = int(arg)

    
    randnums = random.sample(range(1,60000),3)
    get_page(randnums,i)
   

if __name__ == "__main__":
    main(sys.argv[1:])


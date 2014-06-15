#!/usr/bin/python
import os
import string, urllib2
import time
from time import sleep
import random

def get_page(page_id):
    url0 = 'http://128.148.16.163/wiki/?curid=' + `page_id[0]`
    url1 = 'http://128.148.16.167/wiki/?curid=' + `page_id[1]`
    url2 = 'http://128.148.16.179/wiki/?curid=' + `page_id[2]`
    #print url1
    
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
    temp = round(os.times()[4])%2

    if temp == 0:
        f = open('delay.txt', 'a')
        f.write(str(delay)+'\n')
        f.closed

def main():

#    dictionary = []
#    f = open('./dic.txt', 'r')
#    for line in f:
#        dictionary.append(line.split('\n')[0])
#    f.close()
    
    while 1 :
        randnums = random.sample(range(1,60000),3)
        get_page(randnums)
        sleep(1)
   

if __name__ == "__main__":
    main()

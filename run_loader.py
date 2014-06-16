#!/usr/bin/python

import sys, os, getopt
import subprocess
from time import sleep
import thread 

def threadLauncher(threadID,t):

    timer = 0

    while timer < t:
        subprocess.Popen(["./request.py", "-i", str(threadID)])
        timer = timer + 2
        sleep(2)
    thread.exit_thread()

def main(argv):

    n = 0

    try:
        opts, args = getopt.getopt(argv,"hn:t:")
    except getopt.GetoptError:
        print 'request generator \n -n <the number of threads>\n -t <simulation time in second>\n'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'request generator \n -n <the number of threads>\n -t <simulation time in second>\n'
            sys.exit()
        elif opt == '-n':
            n = int(arg)
        elif opt == '-t':
            t = int(arg)

    for i in range(n):
        try:
            thread.start_new_thread(threadLauncher,(i,t))
        except:
            print "Can not create thread"+str(i)+"\n"        
    sleep(t)

if __name__ == "__main__":
    main(sys.argv[1:])

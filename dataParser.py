#!/usr/bin/python

import sys, getopt
import matplotlib.pyplot as plt

'''

-n <the number of experiments> 
-s <the server number>
-p <the plot option> 


Plot options:

'CPU'      : get the CPU utilization of server $s over $n experiment. 
'NET'      : get the networks utilization of server $s over $n experiment. 
'LLC'      : get the total LLC misses of server $s over $n experiment. 
'ITEMS'    : get the number of items on cache server $s over $n experiment.  
'MISSRATE' : get the miss rate of cache server $s over $n experiment. 
'GET'      : get the number of GET operations on cache server $s over $n experiment. 
'CMPITEM_TOT'  : compare the number of items on each cache server.
'CMPITEM'  : compare the number of items on each cache server.
'CMPGET'   : compare the number of GET ops received by each cache server.
'DELAY'    : Plot the mean response during each experiment.  



'''

#----------------Parser functions---------------------------#

def parseServerUtil(inputFile):
    f = open(inputFile,"r")

    temp = f.readline() #get rid of the header

    data = [map(float,line.split()) for line in f]
    # data = []
    # for line in f:
    #     a = [map(float, line.split())]
    #     data = [data,a]
    # print data


    tempData = map(sum,zip(*data))
    length = float(len(data))
    col_sum = [v/length for v in tempData]


    #print col_sum  #for debugging
  
    cpu_util = col_sum[0]
    mem_util = col_sum[1]
    net_util = col_sum[5]

    LLC = sum(col_sum[7:21:2])
    output = [cpu_util, mem_util, net_util, LLC]

    return output


def parseMemcacheStats(inputFile):
    f = open(inputFile,"r")
    temp = f.readline()
    data = [map(float,line.split()) for line in f]

# cumulative stats

    # numItems = data[-1][1]
    # curItems = data[-1][9] 
    # numCmdSet = data[-1][4]
    # numCmdGet = data[-1][5]
    # missRate = data[-1][6]/numCmdGet

# delta stats

    numItems = data[-1][1] - data[0][1] 
    curItems = data[-1][9] - data[0][9] 
    numCmdSet = data[-1][4] - data[0][4] 
    numCmdGet = data[-1][5] - data[0][5] 
    missRate = (data[-1][6] - data[0][6])/numCmdGet


    output = [numItems, numCmdSet,  numCmdGet, missRate, curItems]

    return output



def parseResponseTime(inputFile):
    f = open(inputFile,"r")
    data = [map(float,line.split()) for line in f]
    responseTime = sum(zip(*data)[0])/float(len(data))

    return responseTime



def expServersStats(expNumber):
    serverUtil = []
  
    serverUtil.append(parseServerUtil("./exp" + str(expNumber) + "/master_result.txt"))
    serverUtil.append(parseServerUtil("./exp" + str(expNumber) + "/node1_result.txt"))
    serverUtil.append(parseServerUtil("./exp" + str(expNumber) + "/node2_result.txt"))
    serverUtil.append(parseServerUtil("./exp" + str(expNumber) + "/node3_result.txt"))
    serverUtil.append(parseServerUtil("./exp" + str(expNumber) + "/node4_result.txt"))
    serverUtil.append(parseServerUtil("./exp" + str(expNumber) + "/node5_result.txt"))
    serverUtil.append(parseServerUtil("./exp" + str(expNumber) + "/node6_result.txt"))
    serverUtil.append(parseServerUtil("./exp" + str(expNumber) + "/node7_result.txt"))

    return serverUtil


def expCachesStats(expNumber):
    cacheUtil = []

    cacheUtil.append(parseMemcacheStats("./exp" + str(expNumber) + "/server1.txt"))
    cacheUtil.append(parseMemcacheStats("./exp" + str(expNumber) + "/server2.txt"))
    cacheUtil.append(parseMemcacheStats("./exp" + str(expNumber) + "/server3.txt"))

    return cacheUtil

#-----------------------------------Plot functions------------------------------------#
def plotCPU(serverData,n,s):
    plt.plot(range(1,n+1),serverData[s][0],'r-')
    plt.ylabel('CPU utilization')
    plt.xlabel('experiment number')
    plt.show()

def plotMEM(serverData,n,s):
    plt.plot(range(1,n+1),serverData[s][1],'r-')
    plt.ylabel('Memory utilization')
    plt.xlabel('experiment number')
    plt.show()

def plotNET(serverData,n,s):
    plt.plot(range(1,n+1),serverData[s][2],'r-')
    plt.ylabel('Networks utilization')
    plt.xlabel('experiment number')
    plt.show()

def plotLLC(serverData,n,s):
    plt.plot(range(1,n+1),serverData[s][3],'r-')
    plt.ylabel('LLC misses')
    plt.xlabel('experiment number')
    plt.show()

def plotITEMs(cacheData,n,s):
    plt.plot(range(1,n+1),cacheData[s][0],'r-')
    plt.ylabel('Number of items')
    plt.xlabel('experiment number')
    plt.show()

def plotMISS(cacheData,n,s):	
    plt.plot(range(1,n+1),cacheData[s][3],'r-')
    plt.ylabel('MissRate')
    plt.xlabel('experiment number')
    plt.show()

def plotGETs(cacheData,n,s):
    plt.plot(range(1,n+1),cacheData[s][2],'r-')
    plt.ylabel('Number of GET ops')
    plt.xlabel('experiment number')
    plt.show()      

def plotDELAY(responseTimes,n):
    plt.plot(range(1,n+1),responseTimes,'r-')
    plt.ylabel('Response Time')
    plt.xlabel('experiment number')
    plt.show()

def compareITEM(cacheData,n):
    r = range(1,n+1)    
    plt.plot(r,cacheData[0][4],'r-',r,cacheData[1][4],'b-',r,cacheData[2][4],'g-')
    plt.ylabel('Number of items')
    plt.xlabel('experiment number')
    plt.legend( ('164', '165', '178') )
    plt.show()

def compareSET(cacheData,n):
    r = range(1,n+1)    
    plt.plot(r,cacheData[0][1],'r-',r,cacheData[1][1],'b-',r,cacheData[2][1],'g-')
    plt.ylabel('Number of SET ops')
    plt.xlabel('experiment number')
    plt.legend( ('164', '165', '178') )
    plt.show()

def compareITEM_TOT(cacheData,n):
    r = range(1,n+1)	
    plt.plot(r,cacheData[0][0],'r-',r,cacheData[1][0],'b-',r,cacheData[2][0],'g-')
    plt.ylabel('Number of items')
    plt.xlabel('experiment number')
    plt.legend( ('164', '165', '178') )
    plt.show()

def compareGET(cacheData,n):
    r = range(1,n+1)	
    plt.plot(r,cacheData[0][2],'r-', r,cacheData[1][2],'b-', r,cacheData[2][2],'g-')
    plt.ylabel('Number of GET ops')
    plt.xlabel('experiment number')
    plt.legend( ('164', '165', '178') )
    plt.show()

def compareMISS(cacheData,n):
    r = range(1,n+1)    
    plt.plot(r,cacheData[0][3],'r-', r,cacheData[1][3],'b-', r,cacheData[2][3],'g-')
    plt.ylabel('Miss rate')
    plt.xlabel('experiment number')
    plt.legend( ('164', '165', '178') )
    plt.show()

def compareCPU(serverData,n):
    r = range(1,n+1)    
    plt.plot(r,serverData[0][0],'r-', r,serverData[3][0],'b-', r,serverData[7][0],'g-', r,serverData[2][0],'c-', r,serverData[5][0],'y-', r,serverData[1][0],'m-', r,serverData[6][0],'k-')
    plt.ylabel('CPU utilization')
    plt.xlabel('experiment number')
    plt.legend( ('163', '167', '179', '166', '164', '165', '178') )
    plt.show()

def compareNET(serverData,n):
    r = range(1,n+1)    
    plt.plot(r,serverData[0][2],'r-', r,serverData[3][2],'b-', r,serverData[7][2],'g-', r,serverData[2][2],'c-', r,serverData[5][2],'y-', r,serverData[1][2],'m-', r,serverData[6][2],'k-')
    plt.ylabel('Networks utilization')
    plt.xlabel('experiment number')
    plt.legend( ('163', '167', '179', '166', '164', '165', '178') )
    plt.show()

def compareLLC(serverData,n):
    r = range(1,n+1)    
    plt.plot(r,serverData[0][3],'r-', r,serverData[3][3],'b-', r,serverData[7][3],'g-', r,serverData[2][3],'c-', r,serverData[5][3],'y-', r,serverData[1][3],'m-', r,serverData[6][3],'k-')
    plt.ylabel('LLC misses')
    plt.xlabel('experiment number')
    plt.legend( ('163', '167', '179', '166', '164', '165', '178') )
    plt.show()


#-----------------------------------Main functions------------------------------------#

def main(argv):
    
    numOfCacheServers = 3
    numOfServers = 8
    n = 0
    s = 0
    isPlot = 0

    try:
        opts, args = getopt.getopt(argv,"hn:s:p:")
    except getopt.GetoptError:
        print 'parse_data.py \n -n <number of experiments>\n -s server number \n-p plot option\n'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'parse_data.py \n -n <number of experiments>\n -s <server number> \n -p <plot option> \n'
            sys.exit()
        elif opt == '-n':
            n = int(arg)
        elif opt == '-s':
            s = int(arg)   
        elif opt == '-p':
            isPlot = 1
            option = arg

    serverData = []
    cacheData = []
    responseTimes = []
    SData = []
    CData = []

    for i in range(n):
        serverData.append(expServersStats(i))
        cacheData.append(expCachesStats(i))
        responseTimes.append( parseResponseTime("./exp" + str(i) + "/delay.txt"))
    
    for j in range(numOfCacheServers):
        CData.append(zip(*(zip(*cacheData)[j])))
    for k in range(numOfServers):    
        SData.append(zip(*(zip(*serverData)[k])))    
       

    if isPlot:
        if option == 'CPU':
            plotCPU(SData,n,s)
        elif option == 'MEM':
            plotMEM(SData,n,s)
        elif option == 'NET':
            plotNET(SData,n,s)
        elif option == 'LLC':
            plotLLC(SData,n,s)  
        elif option == 'ITEMS':
            plotITEMs(CData,n,s)
        elif option == 'MISSRATE':
            plotMISS(CData,n,s)
        elif option == 'GET':
            plotGETs(CData,n,s)
        elif option == 'DELAY':  
            plotDELAY(responseTimes,n)
        elif option == 'CMPITEM':
            compareITEM(CData,n) 
        elif option == 'CMPITEM_TOT':
            compareITEM_TOT(CData,n)                
        elif option == 'CMPGET':
            compareGET(CData,n)     
        elif option == 'CMPSET':
            compareSET(CData,n) 
        elif option == 'CMPCPU':
            compareCPU(SData,n) 
        elif option == 'CMPNET':
            compareNET(SData,n)             
        elif option == 'CMPLLC':
            compareLLC(SData,n) 
        elif option == 'CMPMISS':
            compareMISS(CData,n) 

if __name__ == "__main__":
    main(sys.argv[1:])




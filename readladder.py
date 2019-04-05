import sys

def readladder(inputfile):
    wlist = []
    qlist = []
    NQ= inputfile.readline().split()
    N = int(NQ[0])
    Q = int(NQ[1])
    for i in range(N):
        wlist.append(inputfile.readline().rstrip())
        
    for i in range(Q):
        qlist.append(inputfile.readline().split())



    print(N)
    print(Q)
    return([wlist, qlist])

print(readladder(sys.stdin))
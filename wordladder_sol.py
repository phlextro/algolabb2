from collections import Counter

w0 = "there"
w1 = "where"
w2 = "input"
w3 = "putin"
w4 = "hello"
wlist = [w0,w1,w2,w3,w4]

n = len(wlist)

def compare2(s1,s2):
    t1 = s1[1:]
    t2 = s2
    for c in t1:
        if c in t2:
            t2 = t2.replace(c,"",1)
        else:
            return 0
    return 1

admat = [[],[],[],[],[]]

for i in range(n):
    for j in range(n):
        io = compare2(wlist[i],wlist[j])
        admat[i].append(io)
for i in range(n):
    print(admat[i])
        
        
        

        
        




n=int(input())
nl=list(map(int,input().split()))
l=[0]*n
t=0
n2=0
while nl:
    for i in range(n2):
        if nl[n2]==0:
            l[n2]=t
            t=0
            nl.remove(0)
        else:
            t+=1
            nl[n2]-=1
        n2+=1
print(*l)
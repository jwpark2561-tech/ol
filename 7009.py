from bisect import bisect_left
n,m=map(int,input().split())
nl=list(map(int,input().split()))
nl.sort()
m_nl=list(map(int,input().split()))
n_nl=[]
for i in m_nl:
    pos =bisect_left(nl,i)
    if not(pos <len(nl)and nl[pos]==i):
        n_nl.append(i)
if len(n_nl)==0:
    print(-1)
else:
    print(*n_nl)
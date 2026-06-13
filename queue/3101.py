from collections import deque
n,k=map(int,input().split())
q=deque([i+1 for i in range(n)])
l=[]
while q and len(q)!=1:
    for i in range(k):
        if i==k-1:
            l.append(q.popleft())
        else:
            q.append(q.popleft())
if q:
    l.append(q[0])
print(*l)
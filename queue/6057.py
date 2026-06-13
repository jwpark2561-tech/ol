from collections import deque
p,n=map(int,input().split())
q=deque()
ans=0
for _ in range(n):
    o=list(map(int,input().split()))
    if o[0]==0:
        q.append((o[1],o[2]))
    else:
        for _ in range(len(q)):
            pp,vv=q.popleft()
            if pp==o[1]:
                ans+=vv
                o[1]=-1
            else:
                q.append((pp,vv))
print(ans)

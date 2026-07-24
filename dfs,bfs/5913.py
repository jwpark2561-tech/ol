from collections import deque
def bfs(a_list,num):
    visit=[-1]*(n+1)
    dq=deque()
    dq.append(1)
    visit[1]=0
    while dq:
        cur=dq.popleft()
        if visit[cur]==2:
            continue
        for next in a_list[cur]:
            if visit[next]==-1:
                visit[next]=visit[cur]+1
                dq.append(next)
    ans=0
    for j in range(2,n+1):
        if 1<=visit[j]<=2:
            ans+=1
    return ans

n=int(input())
m=int(input())
edges=[]
ans=0
adj=[[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s,m=map(int,input().split())
    edges.append((s,m))
for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)
print(bfs(adj,n))
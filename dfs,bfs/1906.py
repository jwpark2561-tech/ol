from collections import defaultdict, deque

n=int(input())
s,e=map(int,input().split())
m=int(input())
r= defaultdict(list)
visited=[-1]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    r[a].append(b)
    r[b].append(a)
visited[s]=0
q=deque()
q.append((s))
while q:
    v=q.popleft()
    for i in r[v]:
        if visited[i]== -1:
            visited[i]=visited[v]+1
            q.append((i))
print(visited[e])
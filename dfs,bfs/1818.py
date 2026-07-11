from collections import defaultdict, deque


n=int(input())
m=int(input())
r= defaultdict(list)
for _ in range(m):
    a,b=map(int,input().split())
    r[a].append(b)
    r[b].append(a)

visited=[0]*(n+1)
ans=[0]
def DFS(k):
    ans=0
    for i in r[k]:
        if visited[i]==0:
            visited[i]=1
            ans+=1
            ans+=DFS(i)
    return ans
visited[1]=1
#print(DFS(1))

q=deque()
q.append(1)
ans=0
while q:
    v=q.popleft()
    for i in r[v]:
        if visited[i]==0:
            visited[i]=1
            ans+=1
            q.append(i)

print(ans)
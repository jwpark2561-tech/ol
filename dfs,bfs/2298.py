from collections import deque
n=int(input())
r=[list(map(int,input().split()))for _ in range(n)]
v=[[0]*n for _ in range(n)]
ans=0
def dfs(x,y,h):
    for dx,dy in zip((1,-1,0,0),(0,0,1,-1)):
        nx=x+dx
        ny=y+dy
        if 0<=nx<n and 0<=ny<n and v[nx][ny]==0:
            v[nx][ny]=1
            dfs(ny,nx,h)
def bfs(x,y,h):
    q=deque()
    q.append(y,x)
    while q:
        for cx,cy in zip((1,-1,0,0),(0,0,1,-1)):
            nx=x+cx
            ny=y+cy
            if 0<=nx<n and 0<=ny<n and v[nx][ny]==0:
                v[nx][ny]=1
                bfs(ny,nx,h)
def solve(h=4):
    ans=0
    for i in range(n):
        for j in range(n):
            if r[i][j]>h and v[i][j]==0:
                v[i][j]=1
                bfs(i,j,h)
                ans+=1
    return ans
m=0
for i in range(n):
    for j in range(n):
        m=max(m,r[i][j])
for i in range(1,m):
    ans=max(ans,solve(i))
    v=[[0]*n for _ in range(n)]
print(ans)
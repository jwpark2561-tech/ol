from collections import deque


n=int(input())
r=[list(map(int,list(input().strip()))) for _ in range(n)]
v=[[0]*n for _ in range(n)]
ans=0
anss=[]
def bfs(x,y):
    q=deque()
    q.append((y,x))
    while q:
        dy,dx=q.popleft()
        for cy,cx in zip((1,-1,0,0),(0,0,1,-1)):
            nx=dx+cx
            ny=dy+cy
            cy
            if 0<=nx<n and 0<=ny<n and r[ny][nx]==1 and v[ny][nx]==0:
                v[ny][nx]=1
                q.append((ny,nx))
def solve():
    global ans
    for i in range(n):
        for j in range(n):
            if r[i][j]==1 and v[i][j]==0:
                bfs(i,j)
                ans+=1
    return ans
print(solve())
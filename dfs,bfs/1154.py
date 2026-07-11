w,h=map(int,input().split())
r=[input()for _ in range(h)]
v=[[0]*w for _ in range(h)]
ans=1

def dfs(y,x):
    global ans
    for dy,dx in zip((1,-1,0,0),(0,0,1,-1)):
        ny=y+dy
        nx=x+dx
        if 0<=ny<h and 0<=nx<w and r[ny][nx]=='.' and v[ny][nx]==0:
            v[ny][nx]=1 
            ans+=1
            dfs(ny,nx)
for i in range(h):
    for j in range(w):
        if r[i][j]=='@':
            dfs(i,j)
print(ans)
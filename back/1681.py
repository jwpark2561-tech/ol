n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
v=[0]*n
v[0]=1
ans=[float('inf')]
def solve(k,t,vv):
    if t==n-1:
        if l[k][0]!=0:
             ans[0]=min(ans[0], vv+l[k][0])
        return
    for i in range(n):
        if l[k][i]!=0 and v[i]==0 and vv+l[k][i]<ans[0]:
            v[i]=1
            solve(i,t+1,vv+l[k][i])
            v[i]=0
solve(0,0,0)
print(*ans)
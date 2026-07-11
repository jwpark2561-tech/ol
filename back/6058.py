n=int(input())
r=[list(input())for _ in range(n)]
v=[[0]*n for _ in range(n)]
b=[0]*n

def solve(k):
    if k==n:
        return 1
    ans=0
    for i in range(n):
        if b[i]==0 and r[k][i]!="#":
            v[k][i] = 1
            b[i] = 1
            ans += solve(k+1)
            v[k][i] = 0
            b[i] = 0

    return ans

print(solve(0))
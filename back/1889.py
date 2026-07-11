n=int(input())

v=[[0]*n for _ in range(n)]
b=[0]*n
cp=[0]*(2*n)
cn=[0]*(2*n)
ans=[0]

def solve(k):
    if k==n:
        ans[0]+=1
        return
    
    for i in range(n):
        if b[i]==0 and cp[k+i]==0 and cn[n-1+k-i]==0:
            v[k][i]=1
            b[i]=1
            cp[k+i]=1
            cn[n-1+k-i]=1

            solve(k+1)

            v[k][i]=0
            b[i]=0
            cp[k+i]=0
            cn[n-1+k-i]=0
solve(0)
print(*ans)
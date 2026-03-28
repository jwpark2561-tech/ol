l=[]
for i in range(100):
    l.append([0]*100)
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            l[i][j]=1
ans=0
for i in range(100):
    for j in range(100):
        if l[i][j]==1:
            ans+=1
print(ans)
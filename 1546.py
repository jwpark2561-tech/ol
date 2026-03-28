n=int(input())
nl=list(map(int,input().split()))
m=max(nl)
total=0
for i in nl:
    total+=i/m*100
print(total/len(nl))
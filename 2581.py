n=int(input())
l=list(map(int,input().split()))
t=int(input())
ans=l
s=1
e=max(l)

def check(k):
    p=0
    for i in l:
        if i>=k:
            p+=k
        else:
            p+=i
    return t>=p
while s<=e:
    mid=(s+e)//2
    result=check(mid)
    if result==True:
        s=mid+1
        ans=mid
    else:
        e=mid-1
print(ans)
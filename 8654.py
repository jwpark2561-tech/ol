n,t=map(int,input().split())
l=list(map(int,input().split()))

ans=10**10
s=1
e=t

def check(k):
    p=0
    for i in l:
        if i>=k:
            p+=k
        else:
            p+=i
    return t<=p
while s<=e:
    mid=(s+e)//2
    result=check(mid)
    if result==True:
        e=mid-1
        ans=mid
    else:
        s=mid+1
print(ans)
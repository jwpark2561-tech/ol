n,m=map(int,input().split())
l=list(map(int,input().split()))

ans=-1
s=max(l)
e=sum(l)

def check(k):
    t=1
    a=0
    for i in l  :
        if a+i>k:
            t+=1
            a=0
            a+=i
        else:
            a+=i
    return m>=t

while s<=e:
    mid=(s+e)//2
    result=check(mid)
    if result==True:
        ans=mid
        e=mid-1
    else:
        s=mid+1
print(ans)
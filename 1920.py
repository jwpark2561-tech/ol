n=int(input())
l=list(map(int,input().split()))
l.sort()

def solve(n):
    s=0
    e=n-1
    ans=0
    while s<=e:    
        mid=(s+e)//2
        if l[mid]==n:
            ans=1
            break
        elif n<l[mid]:
            e=mid-1
        else:
            s=mid+1
    print(ans)
m=int(input())
ml=list(map(int,input().split()))
for i in ml:
    solve(i)
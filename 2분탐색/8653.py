n,q=map(int,input().split())
l=list(map(int,input().split()))
tv=0
tidx=0
for  i in range(n):
    if l[i]>tv:
        tv=l[i]
        tidx=i
L=l[:tidx]
Lset=set(L)
R=l[tidx+1:]
Rset=set(R)
def isLset(k):
    s=0
    e=tidx-1
    while s<=e:
        mid=(s+e)//2
        if l[mid]==k:
            return True
        elif l[mid]<k:
            s=mid+1
        else:
            e=mid-1
    return False
def isRset(k):
    s=tidx+1
    e=n-1
    while s<=e:
        mid=(s+e)//2
        if l[mid]==k:
            return True
        elif l[mid]<k:
            e=mid-1
        else:
            s=mid+1
    return False
def solve(k):
    #k를 받아서, T, R, N을 호출하는 함수
    if k==tv:
        print("T")
    elif isLset(k):
        print('L')
    elif isRset(k):
        print('R')
    else:
        print('N')
for _   in range(q):
    a=int(input())
    solve(a)
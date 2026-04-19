import sys
input=sys.stdin.readline
n,m=map(int,input().split())
l=list(map(int,input().split()))
#1.시작점(s)과 끝점(e) 정하기
s=0
e=2000000000
while True:
    if s<e:
        break
    #2.중간(mid)정하기
    mid=(s+e)//2
    #3.잘라서 확인(ans)
    ans=0
    aans=0
    for i in l:
        ans+= max(i-mid,0)
    #4.답인지 확인, 아니면 시작점과 끝점 정하기
    if ans>=m:
        aans=mid
        s=mid+1
    elif ans>m:
        s=mid+1
    else:
        e=mid-1
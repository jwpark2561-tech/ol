t,k=map(int,input().split())

def solve():
    print('YES')
    if k==0:
        return 
    n=int(input())
    s=list(input())
    cnt=0
    ans=[]
    while s:
        last=s.pop()
        real=''
        if cnt%2==0:
            real=last
        else:
            if last=='O':
                real='M'
            else:
                real='O'
        ans.append(real)
        if real=='O':
            cnt+=1
    print(*ans[::-1],sep='')


for _ in range(t):
    solve()
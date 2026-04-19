n=int(input())
l=[]
for _ in range(n):
    s=input()
    for i in s:
        if i=='(':
            l.append(i)
        elif i==')':
            if len(l)==0:
                print('NO')
                break
            l.pop()
    if len(l)==0:
        print('YES')
    else:
        print('NO')
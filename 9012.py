n=int(input())
l=[]
result = True
for _ in range(n):
    s=input()
    for i in s:
        if i=='(':
            l.append(i)
            print(l)
        elif i==')':
            if len(l)==0:
                result = False
                break
            l.pop()
            print(l)
    if result == False:
        print('NO')
    else:
        if len(l)==0:
            print('YES')
        else:
            print('NO')
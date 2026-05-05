n=int(input())


for _ in range(n):
    l=[]
    result = True
    s=input()
    for i in range(len(s)):
        if s[i]=='(':
            l.append(s[i])
            #print(l)
        elif s[i]==')':
            if len(l)==0:
                result = False
                break
            l.pop()
            #print(l)
    if result == False:
        print('NO')
    else:
        if len(l)==0:
            print('YES')
        else:
            print('NO')
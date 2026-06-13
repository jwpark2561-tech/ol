l=list()
n=int(input())
for i in range(n):
    s=input().split()
    if s[0]=='i':
        l.append(s[1])
    elif s[0]=='o':
        if l:
            print(l.pop(0))
        else:
            print('empty')
    else:
        print(len(l))
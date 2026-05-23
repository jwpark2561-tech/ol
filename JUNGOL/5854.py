n=int(input())
sl=[]
sl2=[]
for i in range(n):
    s=input()
    if s=='READ':
        sl2.append(sl[-1])
        sl.pop()
    else:
        sl.append(s)
for j in sl2:
    print(j)
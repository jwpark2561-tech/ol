nl=list(map(int,input().split()))
num=0
for i in nl:
    n=nl.count(i)
    if n==2:
        print(1000+i*100)
        break
    elif n==3:
        print(10000+i*1000)
        break
    elif n==1:
        num+=1
        if num==3:
            print(100*max(nl))

def binary_search(data,target):
    l,r=0,len(data)-1
    
    while l<=r:
        m=(l+r)//2
        if data[m]==target:
            return m
        elif data[m]<target:
            l=m+1
        else:
            r=m-1

    return -1
n=int(input())
nl=list(map(int,input().split()))
m=int(input())
m_nl=list(map(int,input().split()))
n_nl=[]
for i in m_nl:
    n_nl.append(binary_search(nl,i))
print(*n_nl)
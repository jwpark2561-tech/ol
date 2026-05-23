n=int(input())
ans=[0]*n
st=[]
l=list(map(int,input().split()))
for  i in range(n-1,-1,-1):
    h=l[i]
    while st and st[-1][1]<h:
        idx,hh=st.pop()
        ans[idx]=i+1
    st.append((i,h))
print(*ans)
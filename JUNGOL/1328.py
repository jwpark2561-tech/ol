n=int(input())
ans=[0]*n
st=[]
for  i in range(n):
    h=int(input())
    while st and st[-1][1]<h:
        idx,hh=st.pop()
        ans[idx]=i+1
    st.append((i,h))
print(*ans,sep='\n')
n=int(input())
ans=0
st=[]
for  i in range(n):
    h=int(input())
    while st and st[-1][1]<h:
        idx,hh=st.pop()
        ans+=i-idx-1
print(ans,st)
lastCow=st[-1][0]
while st:
    idx,_=st.pop()
    ans+=lastCow-idx
print((ans))
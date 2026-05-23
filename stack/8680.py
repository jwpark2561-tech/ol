n=int(input())
s=input()
st=[]
t=0
for i in s:
    if i=="(": 
        st.append(i)
    else: #닫는 괄호라면
        if st:
            if st[-1]=="(":
                st.pop()
        else:
            t+=1
        st.append('(')
print(t)
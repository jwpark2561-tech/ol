from collections import deque
n=int(input())
queue=deque()
ans_max=0
ans=[]
for _ in range(n):
    s=input().split()
    if s[0]=="buy":
        if queue:
            ans.append(queue.popleft())
    elif s[0]=="count":
        ans.append(len(queue))
    elif s[0]=='wait':
           queue.append(int(s[1]))
print(*ans)
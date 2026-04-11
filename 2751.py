import sys
input=sys.stdin.readline
n=int(input())
nl=[]
for _ in range(n):
    a=int(input())
    nl.append(a)
nl.sort()
print(*nl,sep='\n')
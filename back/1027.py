n =int(input())
def is_ok(s):
    l=len(s)
    for i in range(1,l//2+1):
        if s[-i:]==s[(-i*2):-i]:
            return False
    return True
def solve(k):
    if len(k)==n:
        print(k)
        exit(0)
    for i in range(1,4):
        temp=k+str(i)
        if is_ok(temp):
            solve(temp)
solve("")
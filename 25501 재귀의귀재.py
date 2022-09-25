# 재귀의 귀재

import sys
input = sys.stdin.readline

def recursion(s,l,r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s,l+1,r-1)

t = int(input())
for _ in range(t):
    s = input().rstrip()
    cnt = 0
    print(recursion(s,0,len(s)-1),cnt)

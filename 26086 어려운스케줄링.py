# 어려운 스케줄링
# Gold 3, deque

from collections import deque
import sys
input = sys.stdin.readline

N,Q,K = map(int,input().split())

stack = deque()
rev = False
srev = True
l,r = 0,0
for _ in range(Q):
    query = tuple(map(int,input().split()))
    if query[0] == 0:
        p = query[1]
        if rev: 
            stack.appendleft(p)
            l,r = l+1,r+1
        else:
            stack.append(p)
    elif query[0] == 1:
        l,r = 0,len(stack)
        srev = not rev
    elif query[0] == 2:
        rev = not rev
stack = list(stack)

result = stack[:l]+sorted(stack[l:r],reverse=srev)+stack[r:]
if rev: result.reverse()

print(result[-K])
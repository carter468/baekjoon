# 최솟값 찾기
# Platinum 5, sliding window

from collections import deque

n,l = map(int,input().split())
q = deque()
for i,x in enumerate(map(int,input().split())):
    while q and q[-1][0] > x:
        q.pop()
    q.append((x,i))
    if q[0][1] <= i-l: q.popleft()
    print(q[0][0],end=' ')
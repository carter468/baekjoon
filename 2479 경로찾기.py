# 경로 찾기
# Gold 4, BFS

from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
idx = {}
code = [-1]*(n+1)
for i in range(1,n+1):
    c = int(input(),2)
    idx[c] = i
    code[i] = c
a,b = map(int,input().split())

path = [0]*(n+1)
q = deque([code[a]])
while q:
    x = q.popleft()
    if idx[x] == b:
        result = [b]
        while b != a:
            b = path[b]
            result.append(b)
        print(*result[::-1])
        break
    for i in range(k):
        nx = x^(1<<i)
        if nx in idx and path[idx[nx]] == 0:
            q.append(nx)
            path[idx[nx]] = idx[x]
else:
    print(-1)
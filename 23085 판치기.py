# 판치기
# Gold 5, BFS

from collections import deque

def solve():
    n,k = map(int,input().split())
    c = input().count('T')

    visit = [-1]*(n+1)
    visit[c] = 0
    q = deque([c])
    while q:
        x = q.popleft()
        if x == n:
            return visit[x]
        for i in range(min(x,k),-1,-1):
            if k-i > n-x: break
            nx = x-i + k-i
            if visit[nx] == -1:
                visit[nx] = visit[x]+1
                q.append(nx)
    return -1

print(solve())
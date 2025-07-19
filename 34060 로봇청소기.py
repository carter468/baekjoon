# 로봇 청소기
# Gold 3, greedy, DFS

import sys
input = sys.stdin.readline

N = int(input())

x = 0
p = 0
s = set()
for _ in range(N):
    y = int(input())
    if y <= p:
        x += 1
    s.add((x,y))
    p = y

count = 0
visited = set()
for x,y in s:
    if (x,y) not in visited:
        count += 1
        visited.add((x,y))
        q = [(x,y)]
        while q:
            x,y = q.pop()
            for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if (nx,ny) in s and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    q.append((nx,ny))
print(count)
print(N)
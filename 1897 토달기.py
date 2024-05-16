# 토달기
# Gold 5, BFS

from collections import deque,defaultdict

d,s = input().split()
dic = defaultdict(list)
for _ in range(int(d)):
    a = input()
    dic[len(a)].append(a)

q = deque([s])
visited = set()
while q:
    x = q.popleft()
    for nx in dic[len(x)+1]:
        i = 0
        for c in nx:
            if c == x[i]: i += 1
            if i == len(x):
                if nx not in visited:
                    q.append(nx)
                    visited.add(nx)
                break
print(x)
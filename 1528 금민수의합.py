# 금민수의 합
# Gold 3, BFS

from collections import deque

n = int(input())

num = [4,7]
for _ in range(5):
    for i in range(len(num)):
        num.append(num[i]*10+4)
        num.append(num[i]*10+7)
num = sorted(set(num))

q = deque([0])
visited = [-1]*(n+1)
visited[0] = 0
while q:
    x = q.popleft()
    if x == n:
        result = []
        c = visited[x]
        while n:
            for a in num:
                while n > 0 and visited[n-a] == c-1:
                    result.append(a)
                    c -= 1
                    n -= a
        print(*result)
        break
    
    for a in num:
        if x+a <= n and visited[x+a] == -1:
            visited[x+a] = visited[x]+1
            q.append(x+a)
else: print(-1)
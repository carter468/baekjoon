# 병약한 윤호
# Gold 5, BFS

from collections import deque

N = int(input())
S = input()

result = 0
q = deque([(0,0)])
visited = set([(0,0)])
while q:
    a,b = q.popleft()
    c = a+b
    result = max(result,c)
    if result == N*3: break
    if S[a] == 'BLD'[c%3] and (a+1,b) not in visited:
        visited.add((a+1,b))
        q.append((a+1,b))
    if S[-1-b] == 'BLD'[c%3] and (a,b+1) not in visited:
        visited.add((a,b+1))
        q.append((a,b+1))
print(result)
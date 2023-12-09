# 스트레이트 스위치 게임
# Gold 3, BFS

from collections import deque

def check():
    for x in c:
        if x != c[0]: return False
    return True

n,k = map(int,input().split())
cube = tuple(map(int,input().split()))
switch = [0]+[tuple(map(int,input().split()))[1:] for _ in range(k)]

q = deque([cube])
visited = {cube:0}
while q:
    c = q.popleft()
    if check():
        print(visited[c])
        break
    for i in range(1,k+1):
        temp = list(c)
        for x in switch[i]:
            temp[x-1] = (temp[x-1]+i)%5
        if tuple(temp) not in visited:
            visited[tuple(temp)] = visited[c]+1
            q.append(tuple(temp))
else:
    print(-1)
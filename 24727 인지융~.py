# 인지융~
# Gold 3, greedy, constructive

N = int(input())
C,E = map(int,input().split())

result = [[0]*N for _ in range(N)]
a = 0
while C:
    for i in range(a+1):
        if i < N and a-i < N:
            result[i][a-i] = 1
            C -= 1
        if C == 0: break
    a += 1

q = [(N-1,N-1)]
visited = [[False]*N for _ in range(N)]
visited[-1][-1] = True
while E:
    if not q: exit(print(-1))
    x,y = q.pop()
    f = False
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < N and 0 <= ny < N and result[nx][ny] == 1:
            f = True
    if f: continue

    E -= 1
    result[x][y] = 2
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx,ny))

print(1)
for r in result:
    print(*r,sep='')
# 그리드 게임
# Gold 5, BFS

n,m = map(int,input().split())
arr = [input() for _ in range(n)]
k = int(input())

count = 0
state = [[0]*3050 for _ in range(3050)]
q = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'o':
            count += 1
            state[i][j] = 1
            q.append((i,j))

for _ in range(k):
    nq = []
    while q:
        x,y = q.pop()
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if state[nx][ny] == 0:
                state[nx][ny] = 1
                count += 1
                nq.append((nx,ny))
    q = nq
print(count)
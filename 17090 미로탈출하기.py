# 미로 탈출하기
# Gold 3, DFS

n,m = map(int,input().split())
arr = [input() for _ in range(n)]

result = 0
q = []
for i in range(m):
    if arr[0][i] == 'U':
        q.append((0,i))
    if arr[-1][i] == 'D':
        q.append((n-1,i))
for i in range(n):
    if arr[i][0] == 'L':
        q.append((i,0))
    if arr[i][-1] == 'R':
        q.append((i,m-1))

while q:
    x,y = q.pop()
    result += 1
    for nx,ny,d in (x+1,y,'U'),(x-1,y,'D'),(x,y+1,'L'),(x,y-1,'R'):
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == d:
            q.append((nx,ny))
            
print(result)
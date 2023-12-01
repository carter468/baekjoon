# 전개도
# Platinum 5, DFS, implementation

def dfs(x,y):
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if nx < 0 or nx == 6 or ny < 0 or ny == 6 or visited[nx][ny] == 1: continue
        visited[nx][ny] = 1

        num = arr[nx][ny]
        if num != 0:
            if i == k:
                if face[num] == 0 or face[num] == s:
                    face[num] = s
                    face[s] = num
                else:
                    print(0)
                    exit()
            else:
                dfs(nx,ny)

dx = (1,-1,0,0)
dy = (0,0,1,-1)
arr = [tuple(map(int,input().split())) for _ in range(6)]

face = [0]*7
for i in range(6):
    for j in range(6):
        s = arr[i][j]
        if s != 0:
            for k in range(4):
                nx,ny = i+dx[k],j+dy[k]
                if 0 <= nx < 6 and 0 <= ny < 6 and arr[nx][ny] != 0:
                    visited = [[0]*6 for _ in range(6)]
                    visited[i][j],visited[nx][ny] = 1,1
                    dfs(nx,ny)

for i in face[1:]:
    if i == 0:
        print(0)
        break
else: print(face[1])
# 미세먼지 안녕!
# Gold 4, implementation, simulation

r,c,t = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(r)]

for i in range(r):
    if room[i][0] == -1:
        ac = i
        break

arr1 = [[[] for _ in range(c)] for _ in range(r)]
arr2 = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            x,y = i+dx,j+dy
            if 0 <= x < r and 0 <= y < c and room[x][y] != -1:
                arr1[i][j].append((dx,dy))
                arr2[i][j] += 1
room[ac][0],room[ac+1][0] = 0,0

for _ in range(t):
    temp = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            k = room[i][j]//5
            temp[i][j] -= k*arr2[i][j]
            for dx,dy in arr1[i][j]:
                temp[i+dx][j+dy] += k
    for i in range(r):
        for j in range(c):
            room[i][j] += temp[i][j]

    for i in range(ac-1,0,-1):
        room[i][0] = room[i-1][0]
    for i in range(c-1):
        room[0][i] = room[0][i+1]
    for i in range(ac):
        room[i][-1] = room[i+1][-1]
    for i in range(c-1,0,-1):
        room[ac][i] = room[ac][i-1]
    
    for i in range(ac+2,r-1):
        room[i][0] = room[i+1][0]
    for i in range(c-1):
        room[-1][i] = room[-1][i+1]
    for i in range(r-1,ac+1,-1):
        room[i][-1] = room[i-1][-1]
    for i in range(c-1,0,-1):
        room[ac+1][i] = room[ac+1][i-1]

result = 0
for i in range(r):
    result += sum(room[i])
print(result)
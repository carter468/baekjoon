# Drop 7
# Gold 4, implementation, simulation

arr = [list(map(int,input().split())) for _ in range(7)]
K = int(input())

result = 99
for i in range(7):
    cur = [arr[j][:] for j in range(7)]
    for j in range(6,-1,-1):
        if cur[j][i] == 0:
            cur[j][i] = K
            break

    count = 0
    while True:
        temp = []
        for x in range(7):
            y = 0
            while y < 7:
                group = []
                while y < 7 and cur[x][y] != 0:
                    group.append((x,y))
                    y += 1
                y += 1
                for a,b in group:
                    if cur[a][b] == len(group): temp.append((a,b))
        
        for y in range(7):
            x = 0
            while x < 7:
                group = []
                while x < 7 and cur[x][y] != 0:
                    group.append((x,y))
                    x += 1
                x += 1
                for a,b in group:
                    if cur[a][b] == len(group): temp.append((a,b))
        
        if not temp: break
        for x,y in temp:
            cur[x][y] = 0

        for y in range(7):       
            for x in range(6,-1,-1):
                if cur[x][y] != 0:
                    nx = x+1
                    while nx < 7 and cur[nx][y] == 0:
                        nx += 1
                    cur[x][y],cur[nx-1][y] = 0,cur[x][y]
        
    count = 0
    for x in range(7):
        for y in range(7):
            if cur[x][y] != 0: count += 1
    result = min(result,count)
print(result)
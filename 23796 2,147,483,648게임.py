# 2,147,483,648 게임
# Gold 5, implementation

arr = [list(map(int,input().split())) for _ in range(8)]
a = input()

if a == 'U':
    for j in range(8):
        k,l = 0,0
        for i in range(8):
            if arr[i][j] == 0: continue
            if arr[i][j] == l:
                arr[k-1][j] = l*2
                l = 0
                arr[i][j] = 0
            else:
                arr[k][j] = arr[i][j]
                l = arr[i][j]
                if i != k: arr[i][j] = 0
                k += 1
elif a == 'D':
    for j in range(8):
        k,l = 7,0
        for i in range(7,-1,-1):
            if arr[i][j] == 0: continue
            if arr[i][j] == l:
                arr[k+1][j] = l*2
                l = 0
                arr[i][j] = 0
            else:
                arr[k][j] = arr[i][j]
                l = arr[i][j]
                if i != k: arr[i][j] = 0
                k -= 1
elif a == 'L':
    for i in range(8):
        k,l = 0,0
        for j in range(8):
            if arr[i][j] == 0: continue
            if arr[i][j] == l:
                arr[i][k-1] = l*2
                l = 0
                arr[i][j] = 0
            else:
                arr[i][k] = arr[i][j]
                l = arr[i][j]
                if j != k: arr[i][j] = 0
                k += 1
elif a == 'R':
    for i in range(8):
        k,l = 7,0
        for j in range(7,-1,-1):
            if arr[i][j] == 0: continue
            if arr[i][j] == l:
                arr[i][k+1] = l*2
                l = 0
                arr[i][j] = 0
            else:
                arr[i][k] = arr[i][j]
                l = arr[i][j]
                if j != k: arr[i][j] = 0
                k -= 1

for r in arr:
    print(*r)
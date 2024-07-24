# 배열 돌리기 4
# Gold 4, implementation, bruteforcing

def permu(idx,result):
    if idx == k:
        rotate(result,arr)
        return
    for i in range(k):
        if i not in result:
            result.append(i)
            permu(idx+1,result)
            result.pop()

def rotate(result,arr):
    global answer
    for idx in result:
        r,c,s = rot[idx]
        r,c = r-1,c-1
        narr = [[0]*m for _ in range(n)]
        for i in range(1,s+1):
            for j in range(c-i,c+i):
                narr[r-i][j+1] = arr[r-i][j]
            for j in range(r-i,r+i):
                narr[j+1][c+i] = arr[j][c+i]
            for j in range(c-i,c+i):
                narr[r+i][j] = arr[r+i][j+1]
            for j in range(r-i,r+i):
                narr[j][c-i] = arr[j+1][c-i]
        for i in range(n):
            for j in range(m):
                if narr[i][j] == 0:
                    narr[i][j] = arr[i][j]
        arr = narr
    for i in range(n):
        answer = min(answer,sum(arr[i]))

n,m,k = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]
rot = [tuple(map(int,input().split())) for _ in range(k)]

answer = 9999
permu(0,[])
print(answer)
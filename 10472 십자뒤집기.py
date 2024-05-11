# 십자뒤집기
# Gold 5, BFS

from collections import deque

def find(arr):
    num = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == '*':
                num |= 1<<(3*i+j)
    return num

for _ in range(int(input())):
    arr = [input() for _ in range(3)]
    end = find(arr)
    start = [['.']*3 for _ in range(3)]
    q = deque([(start,0)])
    visited = set([find(start)])
    while q:
        arr,count = q.popleft()
        if find(arr) == end:
            print(count)
            break
        for i in range(3):
            for j in range(3):
                narr = [['']*3 for _ in range(3)]
                for ii in range(3):
                    for jj in range(3):
                        narr[ii][jj] = arr[ii][jj]
                for ni,nj in (i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1):
                    if 0 <= ni < 3 and 0 <= nj < 3:
                        if arr[ni][nj] == '*': narr[ni][nj] = '.'
                        else: narr[ni][nj] = '*'
                k = find(narr)
                if k not in visited:
                    visited.add(k)
                    q.append((narr,count+1))
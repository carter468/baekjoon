# ASM – The Abelian Sandpile Model
# Gold 4, implementation

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x,y,n,h = map(int,input().split())
    arr = [list(map(int,input().strip())) for _ in range(x)]
    q = []
    for _ in range(n):
        a,b = map(int,input().split())
        a,b = a-1,b-1
        if arr[a][b] == h: q.append((a,b))
        arr[a][b] += 1
    
    while q:
        a,b = q.pop()
        if arr[a][b] <= h: continue
        c = (arr[a][b]-h-1)//4+1
        d = arr[a][b]-c*4
        arr[a][b] = d
        for i,j in (a+1,b),(a-1,b),(a,b+1),(a,b-1):
            if 0 <= i < x and 0 <= j < y:
                arr[i][j] += c
                if arr[i][j] > h: q.append((i,j))
    
    for a in arr:
        print(''.join(map(str,a)))
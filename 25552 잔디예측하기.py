# 잔디 예측하기
# Gold 3, DFS

import sys
input = sys.stdin.readline

def solve():
    n,m = map(int,input().split())
    A = [list(input()) for _ in range(n)]
    d = int(input())
    B = [input() for _ in range(n)]
    
    q = []
    for i in range(n):
        for j in range(m):
            if A[i][j] == 'O':
                q.append((i,j))
    while q:
        x,y = q.pop()
        for a in range(d+1):
            for b in range(d-a+1):
                for nx,ny in (x+a,y+b),(x-a,y+b),(x+a,y-b),(x-a,y-b):
                    if 0 <= nx < n and 0 <= ny < m and A[nx][ny] == 'X' and B[nx][ny] == 'O':
                        A[nx][ny] = 'O'
                        q.append((nx,ny))
    
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]: return 'NO'
    return 'YES'

print(solve())
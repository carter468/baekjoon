# 채굴
# Gold 3, binary search, DFS

import sys
input = sys.stdin.readline

def check(x):
    s = set()
    visited = [[False]*M for _ in range(N)]
    for j in range(M):
        if S[0][j] <= x:
            s.add((0,j))
            visited[0][j] = True
    for i in range(N):
        for j in (0,M-1):
            if S[i][j] <= x:
                s.add((i,j))
                visited[i][j] = True

    count = 0
    while s:
        i,j = s.pop()
        count += 1
        for ni,nj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and S[ni][nj] <= x:
                s.add((ni,nj))
                visited[ni][nj] = True

    return count >= K

N,M,K = map(int,input().split())
S = [tuple(map(int,input().split())) for _ in range(N)]

no,yes = 0,10**6
while no+1 < yes:
    mid = (no+yes)//2
    if check(mid): yes = mid
    else: no = mid
print(yes)
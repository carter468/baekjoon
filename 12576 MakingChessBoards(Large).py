# Making Chess Boards (Large)
# Platinum 3, DP, priority queue

import sys,heapq
input = sys.stdin.readline

def search(r1,r2,c1,c2):
    for i in range(r1,r2):
        for j in range(c1,c2):
            if 0 <= i < M and 0 <= j < N:
                if grid[i][j] == None:
                    dp[i][j] = 0
                elif i == 0 or j == 0:
                    dp[i][j] = 1
                elif grid[i][j] != grid[i-1][j] and grid[i][j] != grid[i][j-1] and grid[i][j] == grid[i-1][j-1]:
                    dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                else:
                    dp[i][j] = 1
                heapq.heappush(heap,(-dp[i][j],i,j))

def block(r1,r2,c1,c2):
    for i in range(r1,r2):
        for j in range(c1,c2):
            if 0 <= i < M and 0 <= j < N:
                grid[i][j] = None

for tc in range(int(input())):
    M,N = map(int,input().split())
    grid = [list(bin(int(input(),16))[2:].zfill(N)) for _ in range(M)]

    dp = [[0]*N for _ in range(M)]
    heap = []
    search(0,M,0,N)
    count = dict()
    while heap:
        x,r,c = heapq.heappop(heap)
        x = -x
        if x != 0 and dp[r][c] == x:
            count[x] = count.get(x,0)+1
            block(r-x+1,r+1,c-x+1,c+1)
            search(r-x+1,r+x+1,c-x+1,c+x+1)
    
    print(f'Case #{tc+1}: {len(count)}')
    for k in sorted(count)[::-1]:
        print(k,count[k])
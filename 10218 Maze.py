# Maze
# Platinum 5, implementation, BFS

from collections import deque
import sys
input = sys.stdin.readline

D = (0,-1),(0,1),(-1,0),(1,0)
L = 'LRUD'

def solve():
    N,M = map(int,input().split())
    grid = [input() for _ in range(N)]

    move = [[-1]*4 for _ in range(N*M)]
    s = set()
    for x in range(N):
        for y in range(M):
            if grid[x][y] == '.':
                k = x*M+y
                s.add(k)
                for i in range(4):
                    dx,dy = D[i]
                    nx,ny = x,y
                    while grid[nx][ny] == '.':
                        nx += dx
                        ny += dy
                    if grid[nx][ny] == '#':
                        move[k][i] = (nx-dx)*M+(ny-dy)
    
    q = deque([(s,'')])
    visited = {frozenset(s)}
    while q:
        s,l = q.popleft()
        if not s: return l
        if len(l) == 10: continue

        for i in range(4):
            ns = set()
            for x in s:
                if move[x][i] != -1:
                    ns.add(move[x][i])
            ns = frozenset(ns)
            if ns not in visited:
                visited.add(ns)
                q.append((ns,l+L[i]))

    return 'XHAE'

print(*[solve() for _ in range(int(input()))],sep='\n')
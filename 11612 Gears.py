# Gears
# Gold 4, DFS, bipartite graph

import sys
input = sys.stdin.readline

def gcd(a,b):
    while b: a,b = b,a%b
    return a

def solve():
    N = int(input())
    gear = [tuple(map(int,input().split())) for _ in range(N)]

    visited = [(0,0) for _ in range(N)]
    visited[0] = (1,1)
    q = [0]
    while q:
        i = q.pop()
        a,b = visited[i]
        for ni in range(N):
            x1,y1,r1 = gear[i]
            x2,y2,r2 = gear[ni]
            if (x1-x2)**2+(y1-y2)**2 == (r1+r2)**2:
                if visited[ni][0] == 0:
                    na,nb = a*r1,-b*r2
                    g = gcd(na,nb)
                    visited[ni] = (na//g,nb//g)
                    q.append(ni)
                elif visited[ni][0]*visited[i][0] > 0:
                    return 'The input gear cannot move.'
    if visited[-1][0] == 0:
        return 'The input gear is not connected to the output gear.'
    else:
        a,b = visited[-1]
        return f'{a}:{b}'
print(solve())
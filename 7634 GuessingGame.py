# Guessing Game
# Platinum 2, bellman-ford

import sys
input = sys.stdin.readline
INF = 10**9

while True:
    N,M,Q = map(int,input().split())
    if N == 0: break

    edge = [(0,i,0) for i in range(1,N+M+1)]
    for _ in range(Q):
        a,b,c,d = input().split()
        a,b,d = map(int,(a,b,d))
        b += N
        if c[0] == '<':
            edge.append((b,a,d))
        else:
            edge.append((a,b,-d))

    result = 'P'
    dist = [0]+[INF]*(N+M)
    for i in range(N+M+1):
        for s,e,d in edge:
            if dist[s] != INF and dist[e] > dist[s]+d:
                dist[e] = dist[s]+d
                if i == N+M:
                    result = 'Imp'

    print(result+'ossible')
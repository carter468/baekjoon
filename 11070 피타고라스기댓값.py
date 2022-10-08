# 피타고라스 기댓값

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    team = [[0,0] for _ in range(n)]
    w = []
    for _ in range(m):
        a,b,p,q = map(int,input().split())
        team[a-1][0] += p
        team[a-1][1] += q
        team[b-1][0] += q
        team[b-1][1] += p
    for s,a in team:
        if s == 0 and a == 0:
            w.append(0)
        else:
            w.append(s**2/(s**2+a**2))
    print(int(max(w)*1000))
    print(int(min(w)*1000))
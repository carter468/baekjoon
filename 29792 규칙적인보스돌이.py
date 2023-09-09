# 규칙적인 보스돌이
# Gold 5, bruteforce

import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
dmg = [int(input()) for _ in range(n)]
boss = sorted([tuple(map(int,input().split())) for _ in range(k)])

result = []
for d in dmg:
    r = 0
    for i in range(1,1<<k):
        t,q = 0,0
        for j in range(k):
            if i&(1<<j):
                t += (boss[j][0]-1)//d+1
                q += boss[j][1]
        if t <= 900:
            r = max(r,q)
    result.append(r)

print(sum(sorted(result)[-m:]))
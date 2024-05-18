# 승리하라
# Gold 4, bruteforcing

import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
score = [0]*(n+1)
arr = []
team = set()
for _ in range(m):
    a,b,c = map(int,input().split())
    if c == 0: 
        arr.append((a,b))
        team.add(a)
        team.add(b)
    elif c == 1: score[a] += 1
    else: score[b] += 1
if k in team: team.remove(k)
x = score[k]
score[k] = 0
M = max(score)

l = len(arr)
count = 0
for i in range(1<<l):
    dic = {}
    for t in team:
        dic[t] = score[t]
    nx = x
    for j in range(l):
        a,b = arr[j]
        if i>>j&1:
            if a == k: nx += 1
            else: dic[a] += 1
        else:
            if b == k: nx += 1
            else: dic[b] += 1
    for a in dic:
        if dic[a] >= nx: break
    else:
        if nx > M:
            count += 1
print(count)
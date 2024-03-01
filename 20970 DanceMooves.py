# Dance Mooves
# Gold 1, DFS, permutation cycle decomposition

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
pos = [[i] for i in range(n+1)]
arr = list(range(n+1))
for _ in range(k):
    a,b = map(int,input().split())
    arr[a],arr[b] = arr[b],arr[a]
    pos[arr[a]].append(a)
    pos[arr[b]].append(b)

result = [0]*(n+1)
v = [0]*(n+1)
for i in range(1,n+1):
    if v[i]:
        result[i] = result[v[i]]
        continue
    prev = 0
    ni = i
    s = {i}
    while True:
        v[prev] = i
        if v[ni]: break
        for a in pos[ni]: s.add(a)
        prev = ni
        ni = pos[ni][-1]
    result[i] = len(s)

print(*result[1:],sep='\n')
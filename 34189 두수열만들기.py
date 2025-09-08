# 두 수열 만들기
# Gold 1, disjoint set, DP, traceback

import sys
sys.setrecursionlimit(10*4)

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N = int(input())
arr = tuple(map(int,input().split()))

pos = dict()
for i,a in enumerate(arr):
    pos[a] = i
s_arr = set(arr)

root = list(range(N*2))
bucket = [{i} for i in range(N*2)]

for i in range(N*2):
    for j in range(21):
        x = (1<<j)^arr[i]
        if x in s_arr:
            k = pos[x]
            a,b = find(i),find(k)
            if a != b:
                root[a] = b
                bucket[b].update(bucket[a])
div = []
for i in range(N*2):
    if find(i) == i:
        div.append((len(bucket[i]),bucket[i]))

dp = [False]*(N+1)
parent = [-1]*(N+1)
dp[0] = True
for i in range(len(div)):
    x = div[i][0]
    for j in range(N,x-1,-1):
        if dp[j-x] and not dp[j]:
            dp[j] = True
            parent[j] = i

if not dp[N]:
    print(-1)
else:
    result = set()
    s = N
    while s:
        idx = parent[s]
        result.update(div[idx][1])
        s -= div[idx][0]

    r1,r2 = [],[]
    for i in range(N*2):
        if i in result:
            r1.append(arr[i])
        else:
            r2.append(arr[i])
    print(*r1)
    print(*r2)
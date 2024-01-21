# 사촌
# Gold 4, tree

import sys
input = sys.stdin.readline

while True:
    n,k = map(int,input().split())
    if n == 0: break
    arr = tuple(map(int,input().split()))

    parent = [0]*1000001
    parent[arr[0]] = -1
    prev = [arr[0]]
    now = []
    i = 0
    for x in arr[1:]:
        if now and x != now[-1]+1:
            i += 1
            if i == len(prev):
                prev = now
                now = []
                i = 0
        now.append(x)
        parent[x] = prev[i]

    gp,p = parent[parent[k]],parent[k]
    count = 0
    for x in arr:
        if x != k and parent[x] != p and parent[parent[x]] == gp: count += 1
    print(count)
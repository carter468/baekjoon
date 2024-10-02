# 전력난
# Gold 4, MST

import sys,heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

while True:
    m,n = map(int,input().split())
    if m == 0: break
    result = 0
    edge = []
    for _ in range(n):
        x,y,z = map(int,input().split())
        result += z
        heapq.heappush(edge,(z,x,y))

    root = list(range(m))
    count = 1
    while count < m:
        z,x,y = heapq.heappop(edge)
        x,y = find(x),find(y)
        if x != y:
            result -= z
            count += 1
            root[x] = y
    print(result)

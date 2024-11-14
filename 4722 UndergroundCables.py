# Underground Cables
# Gold 3, MST

import sys,heapq
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

while True:
    n = int(input())
    if n == 0: break

    arr = [tuple(map(int,input().split())) for _ in range(n)]
    edge = []
    for i in range(n):
        for j in range(i+1,n):
            d = ((arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2)**0.5
            heapq.heappush(edge,(d,i,j))
    
    root = list(range(n))
    result = 0
    while n > 1:
        d,i,j = heapq.heappop(edge)
        i,j = find(i),find(j)
        if i != j:
            n -= 1
            result += d
            root[i] = j
    print(result)
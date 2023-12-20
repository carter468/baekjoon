# Watering the Fields
# Gold 3, MST

import sys,heapq
input = sys.stdin.readline

n,c = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]

edge = []
for i in range(n):
    for j in range(i+1,n):
        d = (arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2
        if d >= c: heapq.heappush(edge,(d,i,j))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

parent = list(range(n))
count = 0
result = 0
while edge:
    d,i,j = heapq.heappop(edge)
    i,j = find(i),find(j)
    if i != j:
        parent[j] = i
        result += d
        count += 1
        if count == n-1: break

print(result if count == n-1 else -1)
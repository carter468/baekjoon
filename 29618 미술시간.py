# 미술 시간
# Gold 3, disjoint set

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

n,q = map(int,input().split())
result = [0]*(n+1)
root = list(range(n+2))
for _ in range(q):
    a,b,x = map(int,input().split())
    while find(a) <= b:
        c = find(a)
        result[c] = x
        root[a] = c+1
        a = c
print(*result[1:])

# priortity queue

# import sys,heapq
# input = sys.stdin.readline

# n,q = map(int,input().split())
# arr = [0]*(n+1)
# for i in range(q):
#     a,b,x = map(int,input().split())
#     if arr[a]: arr[a].append((i,b,x))
#     else: arr[a] = [(i,b,x)]

# heap = []
# for i in range(1,n+1):
#     if arr[i]:
#         for a in arr[i]:
#             heapq.heappush(heap,a)
#     while heap and heap[0][1] < i:
#         heapq.heappop(heap)    
#     if heap: arr[i] = heap[0][2]

# print(*arr[1:])

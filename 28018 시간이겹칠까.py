# 시간이 겹칠까?
# Gold 5, priority queue

import heapq

n = int(input())
arr = sorted([tuple(map(int,input().split())) for _ in range(n)])

count = [0]*1000001
q = []
j = 0
for i in range(1,1000001):
    while j < n and arr[j][0] == i:
        heapq.heappush(q,arr[j][1])
        j += 1
    count[i] = len(q)
    
    while q and q[0] == i:
        heapq.heappop(q)

input()
for a in map(int,input().split()):
    print(count[a])

# imos법

# count = [0]*1000002
# for _ in range(int(input())):
#     s,e = map(int,input().split())
#     count[s] += 1
#     count[e+1] -= 1
# for i in range(1000001):
#     count[i+1] += count[i]

# input()
# for a in map(int,input().split()):
#     print(count[a])
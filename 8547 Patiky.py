# Patiky
# Gold 5, greedy, priority queue

import heapq

input()
arr = list(map(int,input().split()))

heapq.heapify(arr)
count = 0
while arr:
    x = heapq.heappop(arr)
    if arr and arr[0] == x:
        heapq.heappush(arr,x+heapq.heappop(arr))
    else:
        count += 1
print(count)
# 좋은 친구
# Gold 4, sliding window

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = [len(input()) for _ in range(n)]

result = 0
count = [0]*22
for i in range(k+1):
    result += count[arr[i]]
    count[arr[i]] += 1
for i in range(n-k-1):
    count[arr[i]] -= 1
    x = arr[i+k+1]
    result += count[x]
    count[x] += 1
print(result)

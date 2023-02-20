# 전구
# Gold 3, LIS

import sys
input = sys.stdin.readline

N = int(input())
arr1 = tuple(map(int,input().split()))
arr2 = [0]*N
for i,x in enumerate(arr1):
    arr2[x-1] = i
arr3 = tuple(map(int,input().split()))
arr4 = [arr2[i-1] for i in arr3]

piles = []
prev = [None] * N
dp = [0] * N

for i in range(N):
    card = arr4[i]
    left, right = 0, len(piles)

    while left < right:
        mid = (left + right) // 2
        if piles[mid][-1] < card:
            left = mid + 1
        else:
            right = mid

    if left == len(piles):
        piles.append([card])
    else:
        piles[left].append(card)

    dp[i] = left
    if left > 0:
        prev[i] = piles[left-1][-1]

lis = []
curr = piles[-1][-1]

while curr is not None:
    lis.append(curr)
    curr_idx = arr4.index(curr)
    curr = prev[curr_idx]

answer = sorted([arr1[x] for x in lis])

print(len(answer))
print(*answer)
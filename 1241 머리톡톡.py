# 머리 톡톡
# Gold 5, number theory

import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(int(input()))]

count = [0]*1000001
for a in arr:
    count[a] += 1

for a in arr:
    result = -1
    k = 1
    while k*k <= a:
        if a%k == 0:
            result += count[k]
            if k*k != a:
                result += count[a//k]
        k += 1
    print(result)
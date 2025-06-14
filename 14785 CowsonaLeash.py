# Cows on a Leash
# Gold 5, greedy

import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    a,b = map(int,input().split())
    arr.append((a+b,a))
arr.sort()

count = 0
p = -1
for e,s in arr:
    if s >= p:
        p = e
        count += 1
print(count)
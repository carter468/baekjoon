# Cow Lineup
# Gold 3, two pointer, coordinate compression

import sys
input = sys.stdin.readline

n = int(input())
num = {}
idx = 0
cows = []
for _ in range(n):
    a,b = map(int,input().split())
    if b not in num:
        num[b] = idx
        idx += 1
    cows.append((a,num[b]))
cows.sort()

c = 1
count = [0]*idx
count[cows[0][1]] = 1
l,r = 0,0
result = 10**9
while True:
    if c == idx:
        result = min(result,cows[r][0]-cows[l][0])
        x = cows[l][1]
        count[x] -= 1
        if count[x] == 0: c -= 1
        l += 1

    if c < idx:
        r += 1
        if r == n: break
        x = cows[r][1]
        if count[x] == 0: c += 1
        count[x] += 1
print(result)
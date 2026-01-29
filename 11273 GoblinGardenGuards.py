# Goblin Garden Guards
# Gold 1, prefix sum

import sys
input = sys.stdin.readline

n = int(input())
goblins = dict()
for _ in range(n):
    x,y = map(int,input().split())
    goblins[(x,y)] = goblins.get((x,y),0)+1

soaked = dict()
for _ in range(int(input())):
    x,y,r = map(int,input().split())
    for i in range(r+1):
        d = int((r*r-i*i)**0.5)
        for y1 in (y-i,y+i):
            if y1 < 0 or y1 > 10000: continue
            if y1 not in soaked: soaked[y1] = []
            soaked[y1].append((max(0,x-d),x+d))

for y in soaked:
    arr = [0]*11111
    for l,r in soaked[y]:
        arr[l] += 1
        arr[r+1] -= 1
    for x in range(10001):
        arr[x] += arr[x-1]
        if arr[x]: n -= goblins.get((x,y),0)

print(n)
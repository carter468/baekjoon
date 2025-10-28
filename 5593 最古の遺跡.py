# 最古の遺跡
# Gold 3, bruteforcing, geometry

import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]

s = set(arr)
result = 0
for i in range(N):
    for j in range(i+1,N):
        x1,y1 = arr[i]
        x2,y2 = arr[j]
        t = x1+y1+x2+y2
        if t%2 == 1: continue
        x3,y3 = (t-y2*2)//2,(t-x1*2)//2
        x4,y4 = (t-y1*2)//2,(t-x2*2)//2
        if (x3,y3) in s and (x4,y4) in s:
            result = max(result,((x1-x2)**2+(y1-y2)**2)//2)

print(result)
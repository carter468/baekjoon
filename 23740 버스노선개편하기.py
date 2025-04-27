# 버스 노선 개편하기
# Gold 5, sweeping

import sys
input = sys.stdin.readline

arr = sorted([tuple(map(int,input().split())) for _ in range(int(input()))])

result = []
l,r,x = arr[0]
for s,e,c in arr:
    if r < s:
        result.append((l,r,x))
        l,r,x = s,e,c
    r = max(r,e)
    x = min(x,c)
result.append((l,r,x))

print(len(result))
for r in result:
    print(*r)
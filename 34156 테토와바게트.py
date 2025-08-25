# 테토와 바게트
# Gold 3, greedy, sweeping

import sys
input = sys.stdin.readline

arr = sorted([tuple(map(int,input().split())) for _ in range(int(input()))],key=lambda x:(x[0],-x[1]))

r,rr = -1,-1
count = 0
for s,e in arr:
    if e <= r: continue
    r = e
    if rr <= s:
        count += 1
        rr = e-1
print(count)
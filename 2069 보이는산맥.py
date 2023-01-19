# 보이는 산맥
# Gold 1, 스위핑

import sys
input = sys.stdin.readline

N = int(input())
mountain = sorted([tuple(map(int,input().split())) for _ in range(N)])

right,area = 0,0

for a,b in mountain:
    if a>=right:    # 겹치지 않는 산
        area += (b-a)**2
        right = b
    elif b>right:   # 일부 겹치는 산
        area += (b-a)**2-(right-a)**2
        right = b

print(area)
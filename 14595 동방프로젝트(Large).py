# 동방 프로젝트 (Large)
# Gold 3, sweeping

import sys
input = sys.stdin.readline

n,m = int(input()),int(input())

result,right = 0,1
for l,r in sorted([tuple(map(int,input().split())) for _ in range(m)]):
    if l <= right:
        right = max(right,r)
    else:
        result += l-right
        right = r
print(result+n-right+1)
# Gardening
# Gold 5, geometry, polygon area

import sys
input = sys.stdin.readline

M = int(input())
p = [tuple(map(int,input().split())) for _ in range(M)]

result = 0
for i in range(M):
    x1,y1 = p[i]
    x2,y2 = p[i-1]
    result += x1*y2-x2*y1

print(abs(result)//2)
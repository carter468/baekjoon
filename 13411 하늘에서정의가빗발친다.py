# 하늘에서 정의가 빗발친다

import sys
input = sys.stdin.readline

n = int(input())
target = []
for i in range(1,n+1):
    x,y,v = map(int,input().split())
    target.append([(x**2+y**2)**0.5/v,i])
target.sort()
for x in target:
    print(x[1])
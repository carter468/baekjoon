# 여왕벌
# Gold 4, simulation, implementation

import sys
input = sys.stdin.readline

m,n = map(int,input().split())

result = [1]*(m*2-1)
for _ in range(n):
    a,b,c = map(int,input().split())

    for i in range(a,a+b):
        result[i] += 1
    for i in range(a+b,a+b+c):
        result[i] += 2

for i in range(m):
    print(result[m-1-i],*result[m:])
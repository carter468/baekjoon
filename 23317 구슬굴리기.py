# 구슬 굴리기
# Gold 5, 수학

import sys
input = sys.stdin.readline

def nCr(a,b):
    if b < 0 or a < b:
        return 0
    r = 1
    for i in range(a,a-b,-1):
        r *= i
    for i in range(2,b+1):
        r //= i
    return r

n = int(input())
arr = sorted([tuple(map(int,input().split())) for _ in range(int(input()))])

result = 1
a = (0,0)
for i,j in arr:
    result *= nCr(i-a[0],j-a[1])
    a = (i,j)

print(result*2**(n-i-1))
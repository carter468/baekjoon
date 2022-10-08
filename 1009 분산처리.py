# 분산처리

import sys
input = sys.stdin.readline

def solve(a,b):
    if b==1:
        return a%10
    if b%2==0:
        return (solve(a,b//2)%10)**2%10
    else:
        return (solve(a,b//2)**2)*a%10

t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    c = solve(a,b)%10
    if c==0:
        print(10)
    else:
        print(c)
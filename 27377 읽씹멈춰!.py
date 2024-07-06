# 읽씹 멈춰!
# Gold 3, divide and conquer

import sys
input = sys.stdin.readline

def solve(n):
    if n == 1: return s
    x = solve(n//2)
    if n%2 == 0: return x+min(t,n//2*s)
    else: return x+min(t,n//2*s)+s

for _ in range(int(input())):
    n = int(input())
    s,t = map(int,input().split())
    print(solve(n))
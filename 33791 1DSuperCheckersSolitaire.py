# 1D Super Checkers Solitaire
# Platinum 5, ad hoc, greedy

import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    X = tuple(map(int,input().split()))
    
    if N%2 == 1: return 'NO'

    x = 0
    while x < N and X[x] == x+1:
        x += 1
        
    c = X[0]-1
    for i in range(N-1):
        c += X[i+1]-X[i]-1

    if N%4 == 2:
        return 'YES' if x <= N//2+1 else 'NO'
    if N%4 == 0:
        return 'YES' if c >= 2 and x <= N//2 else 'NO'

for _ in range(int(input())):
    print(solve())
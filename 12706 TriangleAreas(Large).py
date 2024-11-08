# Triangle Areas (Large)
# Gold 3, number theory, constructive

import sys
input = sys.stdin.readline

for t in range(int(input())):
    n,m,a = map(int,input().split())
    if n*m < a: print(f'Case #{t+1}: IMPOSSIBLE')
    elif a%n == 0: print(f'Case #{t+1}: 0 0 {n} 0 0 {a//n}')
    else: print(f'Case #{t+1}: 0 0 {n} 1 {(n*m-a)%n} {1+a//n}')
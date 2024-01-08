# 로봇융합관 건설
# Platinum 2, game theory

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int,input().split())
    if n <= 2 or m <= 2: print('First')
    elif n%2 == 1 and m%2 == 1: print('First')
    else: print('Second')
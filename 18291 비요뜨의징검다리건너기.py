# 비요뜨의 징검다리 건너기
# Gold 5, math, exponentiation by squaring

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    print(pow(2,N-2,10**9+7) if N > 1 else 1)
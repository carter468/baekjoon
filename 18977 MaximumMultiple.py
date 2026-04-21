# Maximum Multiple
# Gold 4, number theory

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    if N%3 == 0:
        print(N**3//27)
    elif N%4 == 0:
        print(N**3//32)
    else:
        print(-1)
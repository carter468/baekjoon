# Load Testing (Small)
# Gold 5, ad hoc

import sys
input = sys.stdin.readline

for t in range(int(input())):
    L,P,C = map(int,input().split())

    x = 0
    while L*C**(2**x) < P:
        x += 1

    print(f'Case #{t+1}: {x}')
# !제곱수 순열
# Gold 5, ad hoc, constructive

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())

    result = list(range(1,N+1))
    for i in range(1,N):
        x = i*2+1
        if int(x**0.5)**2 == x:
            result[i-2],result[i-1] = result[i-1],result[i-2]
    print(*result)
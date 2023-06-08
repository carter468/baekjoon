# 연속 합
# Gold 3, 수학

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    result = 0
    i = 2
    while i*(i+1)//2 <= n:
        if (i%2 == 0 and n%i == i//2) or (i%2 == 1 and n%i == 0):
            result += 1
        i += 1
    print(result)
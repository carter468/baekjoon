# 쿠의 용돈 인상 계획
# Gold 2, greedy

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    D,K = map(int,input().split())
    N = list(input().strip())

    a = 0
    for i in range(D-1,-1,-1):
        if int(N[i]) > 1:
            a = i
            break
    x = int(N[a])
    
    r1 = []
    r2 = []
    for _ in range(K):
        x *= 9
        if x%10 == 1:
            r2.append('1')
            x //= 10
        else:
            r1.append(str(x//10))
            x %= 10

    print(int(''.join(N[:a]+r1+[str(x)]+r2[::-1]+N[a+1:])))
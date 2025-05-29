# 서로소 조합
# Gold 1, math

import sys
input = sys.stdin.readline

def f(a,b,p):
    def g(x):
        c = 0
        i = 1
        while p**i <= x:
            c += x//(p**i)
            i += 1
        return c

    return g(a)-g(b)-g(a-b)

M = 5000
seive = [True]*M
for i in range(2,int(M**0.5)):
    if seive[i]:
        for j in range(i*i,M,i):
            seive[j] = False
prime = []
for i in range(2,M):
    if seive[i]: prime.append(i)

for _ in range(int(input())):
    n1,r1,n2,r2 = map(int,input().split())
    for p in prime:
        if f(n1,r1,p) and f(n2,r2,p):
            print(0)
            break
    else: print(1)
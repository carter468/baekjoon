# 서로소
# Gold 1, 정수론, 비트마스킹, (오일러 피 함수)

import sys

MAX = int(10**4.5)+1
seive = [True]*MAX
for i in range(2,int(MAX**0.5)+1):
    if seive[i]:
        for j in range(i*i,MAX,i):
            seive[j] = False
    
while n:=int(sys.stdin.readline()):
    p = set()
    m = n-1
    while n!=1:
        i = 2
        while i<MAX:
            if seive[i] and n%i==0:
                p.add(i)
                n //= i
                break
            i += 1
        else:
            p.add(n)
            break
    p = tuple(p)
    l = len(p)
    result = 0
    for i in range(1,1<<l):
        k = 1
        c = -1
        for j in range(l):
            if i&(1<<j):
                k *= p[j]
                c *= -1
        result += m//k*c

    print(m-result)
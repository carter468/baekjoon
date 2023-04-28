# 환상의 짝꿍
# Gold 3, 정수론, 소수판정

import sys
input = sys.stdin.readline
MAX = 2000001

def isprime(a):
    for p in prime:
        if p >= a: return 1
        if a%p == 0: return 0
    return 1

seive = [1]*MAX
prime = []
for i in range(2,MAX):
    if seive[i]:
        prime.append(i)
        for j in range(i*i,MAX,i):
            seive[j] = 0

for _ in range(int(input())):
    a = sum(map(int,input().split()))
    if a < 4:
        print('NO')
    elif a%2 == 0:
        print('YES')
    else:
        print('YES' if isprime(a-2) else 'NO')
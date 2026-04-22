# 어려운 소인수분해
# Gold 4, sieve, number theory

M = 5_000_000
sieve = [True]*M
prime = []
for i in range(2,int(M**0.5)+1):
    if sieve[i]:
        for j in range(i*i,M,i):
            sieve[j] = False
        prime.append(i)

input()
for k in map(int,input().split()):
    result = []
    for p in prime:
        while k%p == 0:
            k //= p
            result.append(p)
    if k > 1: result.append(k)
    print(*result)
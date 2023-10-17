# 서로소
# Gold 1, inclusion and exclusion, math

from itertools import combinations

for t in range(int(input())):
    a,b,n = map(int,input().split())
    a -= 1

    f = []
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            f.append(i)
            while n%i == 0:
                n //= i
    if n != 1: f.append(n)

    result = b-a
    for i in range(1,len(f)+1):
        for comb in combinations(f,i):
            k = 1
            for j in comb:
                k *= j
            if i%2 == 1:
                result -= b//k-a//k
            else:
                result += b//k-a//k

    print(f'Case #{t+1}: {result}')
# Factovisors
# Gold 4, math, number theory

from collections import defaultdict

while True:
    try:
        n,m = map(int,input().split())
        if m == 0:
            print(f'{m} does not divide {n}!')
            continue

        x = m
        dic = defaultdict(int)
        for i in range(2,int(m**0.5)+1):
            while x%i == 0:
                x //= i
                dic[i] += 1
        if x > 1: dic[x] += 1

        for a in dic:
            count = 0
            b = a
            while b <= n:
                count += n//b
                b *= a
            if count < dic[a]:
                print(f'{m} does not divide {n}!')
                break
        else:
            print(f'{m} divides {n}!')
    except:
        break

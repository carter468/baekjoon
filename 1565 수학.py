# 수학
# Gold 4, number theory

from collections import defaultdict

def factorize(a):
    temp = defaultdict(int)
    i = 2
    while i*i <= a:
        while a%i == 0:
            temp[i] += 1
            a //= i
        i += 1
    if a > 1: temp[a] = 1
    return temp

input()
lcm = defaultdict(int)
for a in map(int,input().split()):
    temp = factorize(a)
    for f in lcm:
        lcm[f] = max(lcm[f],temp[f])
    for f in temp:
        lcm[f] = max(lcm[f],temp[f])

g = 0
for a in map(int,input().split()):
    if g == 0: g = a
    else:
        while a:
            g,a = a,g%a
gcd = factorize(g)

result = 1
for f in gcd:
    result *= max(0,gcd[f]-lcm[f]+1)
for f in lcm:
    if gcd[f] == 0: result = 0
print(result)
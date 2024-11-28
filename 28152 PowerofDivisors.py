# Power of Divisors
# Gold 2, number theory

from collections import defaultdict

def GCD(a,b):
    while b:
        a,b = b,a%b
    return a

x = int(input())

if int(x**0.5)**2 == x:
    y = int(x**0.5)
    for i in range(2,int(y**0.5)+1):
        if y%i == 0: break
    else: 
        print(y)
        exit()

count = defaultdict(int)
for i in range(2,int(x**0.25)+1):
    while x%i == 0:
        count[i] += 1
        x //= i
if x > 1: count[x] += 1

g = 0
for i in count:
    if g == 0: g = count[i]
    else: g = GCD(g,count[i])

for i in range(g,0,-1):
    if g%i == 0:
        k = 1
        for j in count:
            k *= count[j]//i+1
        if k == i:
            result = 1
            for j in count:
                result *= j**(count[j]//i)
            print(result)
            break
else: print(-1)
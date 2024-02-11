# 구간 성분
# Gold 1, hashing

from collections import defaultdict

def isprime(x):
    if x == 2: return True
    if x%2 == 0: return False
    for i in range(3,int(x**0.5)+1,2):
        if x%i == 0: return False
    return True

MOD = 10**9+7
prime = []
for i in range(2,300):
    if isprime(i): prime.append(i)

a,b = input(),input()

n,m = len(a),len(b)
h = defaultdict(list)
for i in range(n):
    x,y = 1,1
    for j in range(i,n):
        k = ord(a[j])-97
        x = x*prime[k]%MOD
        y = y*prime[k+26]%MOD
        h[x].append((y,j-i))

result = 0
for i in range(m):
    x,y = 1,1
    for j in range(i,m):
        k = ord(b[j])-97
        x = x*prime[k]%MOD
        y = y*prime[k+26]%MOD
        if (y,j-i) in h[x]:
            result = max(result,j-i+1)
print(result)
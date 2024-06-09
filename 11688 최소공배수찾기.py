# 최소공배수 찾기
# Gold 5, number theory

from collections import defaultdict

def f(n):
    result = defaultdict(int)
    for i in range(2,int(n**0.5)+1):
        while n%i == 0:
            n //= i
            result[i] += 1
    if n > 1: result[n] += 1
    return result

a,b,L = map(int,input().split())

fa,fb,fL = f(a),f(b),f(L)
result = 1
for i in fa:
    if fa[i] > fL[i]: result = -1
for i in fb:
    if fb[i] > fL[i]: result = -1

if result != -1:
    for i in fL:
        if fL[i] > max(fa[i],fb[i]):
            result *= i**fL[i]
print(result)
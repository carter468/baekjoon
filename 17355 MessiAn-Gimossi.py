# Messi An-Gimossi
# Gold 2, number theory

import sys
input = sys.stdin.readline
MOD = 10**9+7

def count(n,dic):
    for i in range(2,int(n**0.5)+1):
        while n%i == 0:
            dic[i] = dic.get(i,0)+1
            n //= i
    if n > 1: dic[n] = dic.get(n,0)+1

def f(dic):
    result = 1
    for x in dic:
        result = result*pow(x,dic[x],MOD)%MOD
    return result

a,b = dict(),dict()
for _ in range(int(input())):
    A,B = map(int,input().split())
    count(B-A,a)
    count(B,b)

for x in a:
    if x in b:
        c = min(a[x],b[x])
        a[x] -= c
        b[x] -= c

print(f(a),f(b))
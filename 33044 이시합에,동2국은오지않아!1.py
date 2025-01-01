# 이 시합에, 동2국은 오지 않아! 1
# Gold 1, bruteforcing, combinatorics

import itertools

def nCr(n,r):
    x = 1
    for i in range(r):
        x = x*(n-i)//(i+1)
    return x

def calc(p):
    if p in v: return 0
    v.add(p)
    x = 1
    for i in range(1,10):
        a = num[i]
        b = p[i]
        if a < b: return 0
        x *= nCr(a,b)
    return x

n = int(input())
arr = tuple(map(int,input().split()))
num = [0]*10
for a in arr:
    num[a] += 1

v = set()
count = 0
for c in itertools.combinations(range(1,10),7):
    x = 1
    p = [0]*10
    for i in c:
        p[i] += 2
    count += calc(tuple(p))

body = []
for i in range(1,10):
    body.append((i,i,i))
    if i < 8: 
        for _ in range(4):
            body.append((i,i+1,i+2))

for i in range(1,10):
    for c in itertools.combinations(body,4):
        p = [0]*10
        p[i] = 2
        for a in c:
            for b in a:
                p[b] += 1
        count += calc(tuple(p))
print(count)
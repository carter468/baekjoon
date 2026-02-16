# Doktor
# Platinum 4, prefix sum, greedy

from collections import defaultdict

N = int(input())
A = tuple(map(int,input().split()))

c = [0]
for i,a in enumerate(A,1):
    c.append(c[-1])
    if i == a: c[-1] += 1

d = [[] for _ in range(N+1)]
e = defaultdict(int)
for i,a in enumerate(A,1):
    if i > a: i,a = a,i
    d[i].append(a)
    e[i+a] += 1

result = -1,0,0
for i,a in enumerate(A,1):
    for j in d[i]:
        x = e[i+j]-(c[j]-c[i-1])
        e[i+j] -= 1
        if x > result[0]: result = x,a,A[j-1]

print(*result[1:])
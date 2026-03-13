# Looking for the Risk Factor
# Platinum 3, sieve, offline queries, fenwick tree

import sys
input = sys.stdin.readline

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result

def update(i):
    while i < M:
        tree[i] += 1
        i += (i&-i)

M = 100001
LPF = [0]*M
bucket = [[] for _ in range(M)]
for i in range(2,M):
    if LPF[i] == 0:
        for j in range(i,M,i):
            LPF[j] = i
    bucket[LPF[i]].append(i)

Q = int(input())
query = []
for i in range(Q):
    n,k = map(int,input().split())
    query.append((k,n,i))

tree = [0]*M
result = [0]*Q
p = 1
for k,n,idx in sorted(query):
    for x in range(p+1,k+1):
        for y in bucket[x]:
            update(y)
    p = k
    result[idx] = prefix_sum(n)

print(*result,sep='\n')
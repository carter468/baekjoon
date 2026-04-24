# 수열과 쿼리 22
# Platinum 4, offline query, fenwick tree

import sys
input = sys.stdin.readline

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result

def update(i,dif):
    while i <= N:
        tree[i] += dif
        i += (i&-i)

N = int(input())
A = [0]+list(map(int,input().split()))
q1,q2 = [],[]
c = 0
for _ in range(int(input())):
    q = tuple(map(int,input().split()))
    if q[0] == 1:
        q1.append(q[1:])
    else:
        k,i,j = q[1:]
        q2.append((k,i,j,c))
        c += 1

tree = [0]*(N+1)
for i in range(1,N+1):
    update(i,A[i])

result = [0]*c
idx = 0
for k,i,j,n in sorted(q2):
    while idx < k:
        pos,val = q1[idx]
        update(pos,val-A[pos])
        A[pos] = val
        idx += 1
    result[n] = prefix_sum(j)-prefix_sum(i-1)
print(*result,sep='\n')
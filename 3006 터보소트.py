# 터보소트
# Platinum 4, fenwick tree

import sys
input = sys.stdin.readline

def prefix_sum(tree,i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result

def update(tree,i):
    while i <= N:
        tree[i] += 1
        i += (i&-i)

N = int(input())
A = [int(input()) for _ in range(N)]

B = [0]*(N+1)
for i,a in enumerate(A,1):
    B[a] = i

tree1 = [0]*(N+1)
tree2 = [0]*(N+1)
t = 1
l,r = 1,N
result = []
while l <= r:
    if t == 1:
        x = B[l]
        y = prefix_sum(tree1,N)-prefix_sum(tree1,x)
        z = prefix_sum(tree2,x)
        update(tree1,x)
        result.append(abs(x+y-z-l))
        l += 1
    else:
        x = B[r]
        y = prefix_sum(tree1,N)-prefix_sum(tree1,x)
        z = prefix_sum(tree2,x)
        update(tree2,x)
        result.append(abs(x+y-z-r))
        r -= 1
    t = -t
print(*result,sep='\n')
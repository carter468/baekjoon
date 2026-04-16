# 나무 심기
# Platinum 4, fenwick tree

import sys
input = sys.stdin.readline
MOD = 10**9+7
M = 200001

def query(i):
    x,y = 0,0
    while i > 0:
        x += tree[i][0]
        y += tree[i][1]
        i -= (i&-i)
    return x,y

def update(a):
    i = a
    while i < M:
        tree[i][0] += a
        tree[i][1] += 1
        i += (i&-i)

tree = [[0,0] for _ in range(M)]
t = 0
result = 1
for i in range(int(input())):
    a = int(input())+1
    b,c = query(a)
    if i > 0: result = result*(t-a*i-(b-a*c)*2)%MOD
    update(a)
    t += a
print(result)
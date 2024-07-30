# 네트워크 연결
# Gold 4, MST

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

n,m = int(input()),int(input())
edge = sorted([tuple(map(int,input().split())) for _ in range(m)],key=lambda x:x[2])

root = list(range(n+1))
result = 0
for a,b,cost in edge:
    a,b = find(a),find(b)
    if a != b:
        if a > b: root[a] = b
        else: root[b] = a
        result += cost
print(result)
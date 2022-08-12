# 최소 스패닝 트리

import sys
input = sys.stdin.readline

v,e = map(int,input().split())
root = [i for i in range(v+1)]
edge = []
for _ in range(e):
    edge.append(list(map(int,input().split())))
edge.sort(key=lambda x:x[2])

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

ans = 0
for a,b,c in edge:
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        if root_a > root_b:
            root[root_a] = root_b
        else:
            root[root_b] = root_a
        ans += c

print(ans)
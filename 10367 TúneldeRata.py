# Túnel de Rata
# Platinum 5, MST

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

for tc in range(int(input())):
    S,L = map(int,input().split())
    edge = sorted([tuple(map(int,input().split())) for _ in range(L)],key=lambda x:-x[2])

    root = list(range(S+1))
    d,m = 0,0
    for a,b,c in edge:
        a,b = find(a),find(b)
        if a != b:
            root[a] = b
        else:
            d += c
            m = max(m,c)
    print(f'Case #{tc+1}:',d,m)
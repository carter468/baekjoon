# 도로
# Gold 3, 최소 스패닝 트리

import sys
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

for _ in range(int(input())):
    N,M,P,Q = map(int,input().split())
    root = [i for i in range(N+1)]
    cost = []
    for _ in range(M):
        u,v,w = map(int,input().split())
        cost.append((w,u,v))
    cost.sort()
    
    answer = 'NO'
    for w,u,v in cost:
        a = find(u)
        b = find(v)
        if a!=b:
            if (P,Q) in [(u,v),(v,u)]:
                answer = 'YES'
                break
            if a<b:
                root[b] = a
            else:
                root[a] = b
    print(answer)
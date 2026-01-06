# 뭉쳐야 산다
# Gold 1, smaller to larger

import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
S = [0]+[set(tuple(map(int,input().split()))[1:]) for _ in range(N)]

empty = [False]*(N+1)
link = list(range(N+1))
for _ in range(Q):
    q = tuple(map(int,input().split()))
    if q[0] == 1:
        a,b = q[1:]
        if empty[b]: continue
        if empty[a]:
            empty[a] = False
            link[a] = link[b]
            empty[b] = True
        else:
            la = link[a]
            lb = link[b]
            if len(S[la]) < len(S[lb]):
                for x in S[la]:
                    S[lb].add(x)
                link[a] = lb
            else:
                for x in S[lb]:
                    S[la].add(x)
            empty[b] = True
    else:
        a = q[1]
        if empty[a]: print(0)
        else: print(len(S[link[a]]))
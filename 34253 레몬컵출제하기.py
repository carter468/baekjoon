# 레몬컵 출제하기
# Platinum 5, bitmask, DFS

import sys
input = sys.stdin.readline

def push(x):
    if x in known: return
    known.add(x)
    for i in range(K):
        if x>>i&1:
            push(x-(1<<i))

N,K = map(int,input().split())

known = set()
z = 0
for _ in range(N):
    s = input().strip()
    if z == 1: s = s[::-1]

    a = 0
    for i in range(K):
        if s[-1-i] == '1': a += 1<<i
    if a in known:
        z = 0
    else:
        z = 1
        push(a)
    print(['WellKnown','AdHoc'][z])
# 팔정도 모니터링
# Gold 3, ternary search

import sys
input = sys.stdin.readline

def f(t):
    res = 0
    p = (0,t),(t,t),(t,0),(t,-t)
    for x,y in speaker:
        for x1,y1 in p:
            res += abs(x-x1)+abs(y-y1)
    return res

N,R = map(int,input().split())
speaker = [tuple(map(int,input().split())) for _ in range(N)]

lo,hi = -R,R
while lo+3 < hi:
    m1 = (lo*2+hi)//3
    m2 = (lo+hi*2)//3
    if f(m1) < f(m2): hi = m2
    else: lo = m1

result = sys.maxsize
for i in range(lo,hi+1):
    result = min(result,f(i))
print(result)
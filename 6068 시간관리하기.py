# 시간 관리하기
# Gold 5, 그리디 알고리즘

import sys
input = sys.stdin.readline

wlist = sorted([list(map(int,input().split())) for _ in range(int(input()))],key=lambda x:x[1])

stime = 1000000
while wlist:
    t,s = wlist.pop()
    if stime<s:
        stime -= t
    else:
        stime = s-t

print(-1 if stime<0 else stime)
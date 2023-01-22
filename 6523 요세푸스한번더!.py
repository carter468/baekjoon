# 요세푸스 한 번 더!
# Gold 1, 그래프 이론

import sys

while True:
    s = sys.stdin.readline().strip()
    if s=='0':
        break
    N,a,b = map(int,s.split())
    order = {}
    x,cnt=0,0
    while x not in order:
        order[x] = cnt
        cnt += 1
        x = (x**2*a+b)%N
    print(N-cnt+order[x])
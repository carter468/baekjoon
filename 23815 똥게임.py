# 똥게임
# Gold 4, DP, greedy

import sys
input = sys.stdin.readline

r1,r2 = 1,0
for i in range(int(input())):
    a,b = input().split()
    t1,t2 = 0,0
    if r1 > 0:
        x = str(r1)
        t1 = max(int(eval(x+a)),int(eval(x+b)))
        t2 = r1
    if r2 > 0:
        x = str(r2)
        t2 = max(t2,int(eval(x+a)),int(eval(x+b)))
    r1,r2 = t1,t2

print(max(r1,r2) if max(r1,r2) > 0 else 'ddong game')
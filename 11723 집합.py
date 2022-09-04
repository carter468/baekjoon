# 집합

import sys
input = sys.stdin.readline

m = int(input())
s = 0
x = []
for _ in range(m):
    operate = list(map(str,input().split()))
    if operate[0] == 'add':
        s = s | (1<<int(operate[1]))
    elif operate[0] == 'remove':
        s = s & ~(1<<int(operate[1]))
    elif operate[0] == 'check':
        if s & (1<<int(operate[1])) == 0:
            print(0)
        else:
            print(1)
    elif operate[0] == 'toggle':
        s = s ^ (1<<int(operate[1]))
    elif operate[0] == 'all':
        s = 2**21 - 1
    else:
        s = 0
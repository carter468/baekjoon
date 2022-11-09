# 팰린드로미터

import sys

while True:
    t = sys.stdin.readline().strip()
    if t=='0':
        break
    u = int(t)
    l = len(t)
    while True:
        s = str(u).zfill(l)
        if s==s[::-1]:
            break
        u += 1
    print(u-int(t))
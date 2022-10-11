# 놀라운 문자열

import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    n = len(s)
    if s=='*':
        break
    surprising = True
    for i in range(n-1):
        pair = []
        for j in range(n-i-1):
            tmp = s[j]+s[j+i+1]
            if tmp in pair:
                surprising = False
                break
            pair.append(tmp)
        if surprising == False:
            break
    if surprising:
        print(f'{s} is surprising.')
    else:
        print(f'{s} is NOT surprising.')
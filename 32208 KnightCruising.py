# Knight Cruising
# Gold 5, ad hoc, math

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    if sum(map(int,input().split()))%2 == 0: print('YES')
    else: print('NO')

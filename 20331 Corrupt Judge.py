# Corrupt Judge
# Gold 5, greedy, case work

import sys

n,p = map(int,input().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]

if arr[0] == 0: p = 0
a = 0
result = []
for t in arr:
    if t < a: p -= 1
    a = t
    result.append(p)
if arr[-1] == 0 and p > 0: print('ambiguous')
elif arr[-1] > 0 and p > 1: print('ambiguous')
else: print(*result,sep='\n')
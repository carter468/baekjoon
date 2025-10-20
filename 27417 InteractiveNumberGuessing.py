# Interactive Number Guessing
# Gold 3, ad hoc, binary search

import sys
input = sys.stdin.readline
M = 17

def check(x):
    print('query',x*d)
    sys.stdout.flush()
    a = int(input())
    return a-b == x

print('query 0')
sys.stdout.flush()
b = int(input())

result,c = 0,0
d = 10**M
for i in range(M):
    lo,hi = 0,10
    while lo+1 < hi:
        mid = (lo+hi)//2
        if check(mid): lo = mid
        else: hi = mid
    result = result*10+9-lo
    c += 9-lo
    d //= 10
result = result*10+b-c
print('answer',result)
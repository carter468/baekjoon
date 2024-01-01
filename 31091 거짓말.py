# 거짓말
# Gold 5, binary search

import bisect

n = int(input())
plus = []
minus = []
for x in map(int,input().split()):
    if x <= 0: minus.append(x)
    else: plus.append(x)
plus.sort()
minus.sort()

result = []
for i in range(n+1):
    a = bisect.bisect_right(plus,i) 
    b = bisect.bisect_right(minus,-i) 
    if a+b == n-i: result.append(i)
print(len(result))
print(*result)
# Draw A Perfect Circle
# Gold 4, two pointer

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = []
for _ in range(n):
    x,y = map(int,input().split())
    arr.append((x*x+y*y)**0.5)
arr.sort()

result = 1
l,r = 0,0
while r < n:
    a,b = arr[l],arr[r]
    if a+k >= b:
        result = max(result,r-l+1)
        r += 1
    else:
        l += 1
print(result*100/n)

# 개똥벌레
# Gold 5, prefix sum

import sys
input = sys.stdin.readline

n,h = map(int,input().split())
arr = [int(input()) for _ in range(n)]

up,down = [0]*(h+1),[0]*(h+1)
for i in range(n):
    a = arr[i]
    if i%2 == 0:
        up[a] += 1
    else:
        down[h-a+1] += 1

for i in range(h):
    up[h-1-i] += up[h-i]
    down[i+1] += down[i]

result = [n,0]
for i in range(1,h+1):
    x = up[i]+down[i]
    if x < result[0]: result = [x,1]
    elif x == result[0]: result[1] += 1
print(*result)

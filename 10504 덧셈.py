# 덧셈
# Gold 3, math

import sys
input = sys.stdin.readline

M = 44721

arr = []
x = 0
for i in range(M):
    x += i
    arr.append(x)

for _ in range(int(input())):
    n = int(input())
    for i in range(2,M):
        if arr[i] > n:
            result = 0
            break
        if (n-arr[i])%i == 0:
            k = (n-arr[i])//i
            result = []
            for j in range(1,i+1):
                result.append(str(j+k))
            break
    
    if result: print(n,'=',' + '.join(result))
    else: print('IMPOSSIBLE')
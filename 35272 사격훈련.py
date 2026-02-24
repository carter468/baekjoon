# 사격 훈련
# Gold 5, probability, combinatorics, bruteforcing

import math

N = int(input())
P,Q = map(float,input().split())

arr = [0]*(N+1)
for i in range(N+1):
    arr[i] = math.comb(N,i)*Q**i*(1-Q)**(N-i)

result = 0
for i in range(N+1):
    arr1 = [0]*(N+1)
    for j in range(i+1):
        arr1[j] = math.comb(i,j)*(P**j)*(1-P)**(i-j)
    x = 0
    for j in range(N+1):
        c = 0
        for k in range(j+1):
            c += arr[k]*arr1[j-k]
        x += c*j
    result = max(result,x)
print(result)
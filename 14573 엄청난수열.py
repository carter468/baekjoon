# 엄청난 수열
# Gold 1, math, DP, prefix sum

import sys
input = sys.stdin.readline
MOD = 10**9+7

psum = [0,1,2]
p = 1
a = 1
for i in range(10**6-2):
    p = p*2%MOD
    a = (p+2)*a%MOD
    psum.append((psum[-1]+a)%MOD)

result = []
for _ in range(int(input())):
    query = tuple(map(int,input().split()))

    if query[0] == 1:
        a1,i,j = query[1:]
        x = min(i,j)
        result.append((psum[x]-psum[x-1])*a1%MOD)

    elif query[0] == 2:
        a1,i,j = query[1:]
        x = max(i,j)
        if x < 3: x = 0
        else: x = x-1
        while a1%2 == 0:
            x += 1
            a1 //= 2
        result.append(x)

    elif query[0] == 3:
        a1,i,j = query[1:]
        if i > j: i,j = j,i
        result.append((psum[j]-psum[i-1])*a1%MOD)

    else:
        a1,k = query[1:]
        result.append((psum[k]-psum[k-1])*a1%MOD)

print(*result,sep='\n')
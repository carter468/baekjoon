# 수들의 합 8
# Gold 3, prefix sum, hash set

from collections import defaultdict

n = int(input())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

count = defaultdict(int)
count[0] = 1
sa,sb = 0,0
result = 0
for i in range(n):
    sa += A[i]
    sb += B[i]
    result += count[sa-sb]
    count[sa-sb] += 1
    
print(result)
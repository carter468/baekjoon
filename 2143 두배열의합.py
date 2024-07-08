# 두 배열의 합
# Gold 3, prefix sum, hash set

from collections import defaultdict

t = int(input())
n = int(input())
a = [0]+list(map(int,input().split()))
m = int(input())
b = [0]+list(map(int,input().split()))

for i in range(n):
    a[i+1] += a[i]
for i in range(m):
    b[i+1] += b[i]

dica,dicb = defaultdict(int),defaultdict(int)
for i in range(1,n+1):
    for j in range(1,i+1):
        dica[a[i]-a[j-1]] += 1
for i in range(1,m+1):
    for j in range(1,i+1):
        dicb[b[i]-b[j-1]] += 1

result = 0
for x in dica:
    result += dica[x]*dicb[t-x]
print(result)
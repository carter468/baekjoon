# 수학은 너무 쉬워
# Gold 3, number theory

from collections import defaultdict

n = int(input())
arr = tuple(map(int,input().split()))

count = [defaultdict(int) for _ in range(n)]
total = defaultdict(int)
for i in range(n):
    a = arr[i]
    for x in range(2,int(a**0.5)+1):
        while a%x == 0:
            count[i][x] += 1
            total[x] += 1
            a //= x
    if a > 1:
        count[i][a] += 1
        total[a] += 1

result,gcd = 0,1
for x in total:
    k = total[x]//n
    gcd *= x**k
    for i in range(n):
        if count[i][x] < k:
            result += k-count[i][x]
print(gcd,result)
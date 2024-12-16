# 카드 뽑기
# Gold 5, probability, combinatorics

from collections import defaultdict
MOD = 10**9+7

N = int(input())
A = tuple(map(int,input().split()))

dic = defaultdict(int)
for a in A:
    dic[a] += 1

result = 1
for a in dic:
    result = result*(dic[a]+1)%MOD
print((result-1)%MOD)
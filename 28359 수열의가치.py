# 수열의 가치
# Gold 5, ad hoc

from collections import defaultdict

n = int(input())
arr = sorted(map(int,input().split()))

dic = defaultdict(int)
for a in arr:
    dic[a] += 1

c = 0
for key in dic:
    c = max(c,key*dic[key])

print(sum(arr)+c)
print(*arr)
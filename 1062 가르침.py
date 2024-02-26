# 가르침
# Gold 4, bruteforcing

import itertools

n,k = map(int,input().split())
arr = [input() for _ in range(n)]

result = 0
k -= 5
if k >= 0:
    for s in itertools.combinations('qweryuopsdfghjklzxvbm',k):
        count = 0
        for a in arr:
            for c in a:
                if c not in 'antic' and c not in s: break
            else: count += 1
        result = max(result,count)
print(result)
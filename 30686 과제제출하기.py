# 과제 제출하기
# Gold 5, bruteforcing

import itertools

n,m = map(int,input().split())
d = tuple(map(int,input().split()))
p = [list(map(int,input().split()))[1:] for _ in range(m)]

result = 10**9
for arr in itertools.permutations(list(range(m)),m):
    count = 0
    v = [-1]*(n+1)
    for i in range(m):
        for a in p[arr[i]]:
            if v[a] < i:
                v[a] = i+d[a-1]-1
                count += 1
    result = min(result,count)
print(result)
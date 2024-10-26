# Dance Recital
# Gold 5, bruteforcing

import itertools

n = int(input())
arr = [set(input()) for _ in range(n)]

change = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        for a in arr[i]:
            if a in arr[j]:
                change[i][j] += 1
                change[j][i] += 1

result = 999
for p in itertools.permutations(range(n)):
    count = 0
    for i in range(n-1):
        count += change[p[i]][p[i+1]]
    result = min(result,count)
print(result)
# 치킨 배달
# Gold 5, bruteforcing

import itertools

n,m = map(int,input().split())
arr = [list(input().split()) for _ in range(n)]

h,c = [],[]
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1': h.append((i,j))
        elif arr[i][j] == '2': c.append((i,j))

result = 10**9
for p in itertools.combinations(c,m):
    a = 0
    for x1,y1 in h:
        b = 10**9
        for x2,y2 in p:
            b = min(b,abs(x1-x2)+abs(y1-y2))
        a += b
    result = min(result,a)
print(result)
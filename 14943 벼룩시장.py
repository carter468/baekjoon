# 벼룩시장
# Gold 3, greedy

from collections import deque

n = int(input())
arr = tuple(map(int,input().split()))

q = deque()
result = 0
for i in range(n):
    k = arr[i]
    if not q: q.append([k,i])
    elif k*q[0][0] > 0:
        q.append([k,i])
    else:
        while q and abs(q[0][0]) <= abs(k):
            a,b = q.popleft()
            k += a
            result += abs(a)*(i-b)
        if k == 0: continue
        if not q:
            q.append([k,i])
        else:
            q[0][0] += k
            result += abs(k)*(i-q[0][1])
print(result)
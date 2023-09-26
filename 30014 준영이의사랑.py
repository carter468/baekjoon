# 준영이의 사랑
# Gold 2, greedy, deque

from collections import deque

input()
p = sorted(map(int,input().split()))[::-1]

q = deque([p[0]])
result = 0
for a in p[1:]:
    if q[0] > q[-1]:
        result += q[0]*a
        q.appendleft(a)
    else:
        result += q[-1]*a
        q.append(a)
print(result+q[0]*q[-1])
print(*q)
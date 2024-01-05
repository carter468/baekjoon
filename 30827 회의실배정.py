# 회의실 배정
# Gold 4, greedy

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = sorted([tuple(map(int,input().split())) for _ in range(n)],key=lambda x:x[1])

q = []
result = 0
for s,e in arr:
    for i in range(len(q)):
        if q[i] < s:
            result += 1
            q[i] = e
            break
    else:
        if len(q) < k:
            result += 1
            q.append(e)
    q.sort(reverse=True)
print(result)
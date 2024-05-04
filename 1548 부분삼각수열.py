# 부분 삼각 수열
# Gold 5, greedy

from collections import deque

input()
arr = sorted(map(int,input().split()))

seq = deque()
result = 0
for a in arr:
    seq.append(a)
    while len(seq) > 2 and seq[0]+seq[1] <= seq[-1]:
        seq.popleft()
    result = max(result,len(seq))
print(result)
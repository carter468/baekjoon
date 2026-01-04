# 낚시 (Easy)
# Gold 3, greedy

from collections import deque

N,M = map(int,input().split())
B = sorted(map(int,input().split()))
F = sorted(map(int,input().split()))

fish = deque()
i = 0
result = 0
for j in range(M):
    if i < N and B[i] < F[j]:
        fish.append(F[j])
        result += F[j]
        i += 1
    elif fish:
        result -= fish.popleft()
        fish.append(F[j])
        result += F[j]
print(result)
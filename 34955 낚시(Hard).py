# 낚시 (Hard)
# Gold 1, constructive, greedy

from collections import deque

N,M = map(int,input().split())
B = sorted(map(int,input().split()))
F = sorted(map(int,input().split()))

fish = deque()
i = 0
result = 0
act = []
for f in F:
    if i < N and B[i] < f:
        act.append(f'fish {B[i]}')
        fish.append(f)
        result += f
        i += 1
    elif fish and fish[0] != f:
        a = fish.popleft()
        act.append(f'bait {a}')
        act.append(f'fish {a}')
        result -= a
        fish.append(f)
        result += f

print(len(act))
if act: print(*act,sep='\n')
print(result)
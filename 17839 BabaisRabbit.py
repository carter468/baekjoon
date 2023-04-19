# Baba is Rabbit
# Gold 5, 그래프 탐색

from collections import defaultdict
import sys
input = sys.stdin.readline

dict = defaultdict(list)
for _ in range(int(input())):
    a,b,c = input().split()
    dict[a].append(c)

q = ['Baba']
result = set()
while q:
    x = q.pop()
    for nx in dict[x]:
        if nx not in result:
            q.append(nx)
            result.add(nx)

if result:
    print('\n'.join(sorted(result)))
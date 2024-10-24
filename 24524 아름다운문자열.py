# 아름다운 문자열
# Gold 5, greedy

from collections import defaultdict,deque

def solve():
    S,T = input(),input()

    dic = defaultdict(deque)
    for i,s in enumerate(S):
        dic[s].append(i)

    count = 0
    while True:
        now = -1
        for t in T:
            while dic[t] and dic[t][0] < now:
                dic[t].popleft()
            if not dic[t]:
                return count
            now = dic[t].popleft()
        count += 1

print(solve())
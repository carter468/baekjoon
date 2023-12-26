# 정보 상인 호석
# Gold 5, priority queue

from collections import defaultdict
import sys,heapq
input = sys.stdin.readline

dic = defaultdict(list)
result = 0
for _ in range(int(input())):
    query = input().split()
    if query[0] == '1':
        for x in query[3:]:
            heapq.heappush(dic[query[1]],-int(x))
    else:
        for _ in range(int(query[2])):
            if dic[query[1]]:
                result -= heapq.heappop(dic[query[1]])
            else:
                break
print(result)
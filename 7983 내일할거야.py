# 내일 할 거야
# Gold 5, 그리디 알고리즘, 우선순위 큐

import sys
input = sys.stdin.readline

data = [tuple(map(int,input().split())) for _ in range(int(input()))]
data.sort(key=lambda x:x[1])

result = 10**9
while data:
    a,b = data.pop()
    result = min(b,result)-a
    
print(result)

# import heapq
# import sys
# input = sys.stdin.readline

# q = []
# for _ in range(int(input())):
#     d,t = map(int,input().split())
#     heapq.heappush(q,(-t,d))

# result = sys.maxsize
# while q:
#     a,b = heapq.heappop(q)
#     result = min(-a,result)-b

# print(result)


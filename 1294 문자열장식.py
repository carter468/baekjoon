# 문자열 장식
# Platinum 3, greedy, priority queue

import heapq

class string:
    def __init__(self,str):
        self.str = str
    def __lt__(self,other):
        return self.str+other.str < other.str+self.str

q = []
for _ in range(int(input())):
    heapq.heappush(q,string(input()))
answer = ''
while q:
    s = heapq.heappop(q).str
    answer += s[0]
    if len(s) > 1:
        heapq.heappush(q,string(s[1:]))
print(answer)


import heapq

c = 0
q = []
for _ in range(int(input())):
    s = input()
    c += len(s)
    heapq.heappush(q,s+'a')
answer = ''
for _ in range(c):
    s = heapq.heappop(q)
    answer += s[0]
    if len(s) > 1:
        heapq.heappush(q,s[1:])
print(answer)
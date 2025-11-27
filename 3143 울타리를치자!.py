# 울타리를 치자!
# Gold 2, greedy, priority queue

import sys,heapq
input = sys.stdin.readline

N = int(input())
A = sorted([(a,i) for i,a in enumerate(map(int,input().split()))]) # 높이,위치
B = sorted([(*map(int,input().split()),i+1) for i in range(N)]) # 높이,가격,번호

result = 0
pos = [0]*N
match = []
remain = []

i = 0
for j in range(N):
    hb,c,idxb = B[j]
    ha,idxa = A[i]
    if ha <= hb:
        result += c
        pos[idxa] = idxb
        heapq.heappush(match,(c,idxa,idxb))
        i += 1
    elif match and match[0][0] < c:
        c1,idxa1,idxb1 = heapq.heappop(match)
        heapq.heappush(match,(c,idxa1,idxb))
        result += c-c1
        pos[idxa1] = idxb
        remain.append(idxb1)
    else:
        remain.append(idxb)

while remain:
    pos[A[i][1]] = remain.pop()
    i += 1

print(result)
print(*pos)
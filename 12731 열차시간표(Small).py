# 열차 시간표(Small)
# Gold 5, priority queue, greedy, implementation, simulation

import heapq

def minute(x):
    h,m = map(int,x.split(':'))
    return h*60+m

for c in range(int(input())):
    t = int(input())
    a,b = map(int,input().split())
    arr = []
    for _ in range(a):
        s,e = input().split()
        arr.append((minute(s),minute(e),1))
    for _ in range(b):
        s,e = input().split()
        arr.append((minute(s),minute(e),2))
    arr.sort()

    w1,w2 = [],[]
    for s,e,i in arr:
        if i == 1:
            if w1 and w1[0] <= s:
                heapq.heappop(w1)
                a -= 1
            heapq.heappush(w2,e+t)
        else:
            if w2 and w2[0] <= s:
                heapq.heappop(w2)
                b -= 1
            heapq.heappush(w1,e+t)
    print(f'Case #{c+1}: {a} {b}')
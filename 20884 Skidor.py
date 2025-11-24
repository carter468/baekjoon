# Skidor
# Platinum 4, deque trick

from collections import deque
import sys
input = sys.stdin.readline

R,C,L = map(int,input().split())
grid = [tuple(map(int,input().split())) for _ in range(R)]

a = []
for i in range(R):
    minq = deque()
    maxq = deque()
    b = []
    for j,x in enumerate(grid[i]):
        while minq and minq[-1][0] > x:
            minq.pop()
        minq.append((x,j))
        if minq[0][1] <= j-L: minq.popleft()
        while maxq and maxq[-1][0] < x:
            maxq.pop()
        maxq.append((x,j))
        if maxq[0][1] <= j-L: maxq.popleft()
        b.append((minq[0][0],maxq[0][0]))
    a.append(b)

result = []
for j in range(L-1,C):
    minq = deque()
    maxq = deque()
    for i in range(R):
        x,y = a[i][j]
        while minq and minq[-1][0] > x:
            minq.pop()
        minq.append((x,i))
        if minq[0][1] <= i-L: minq.popleft()
        while maxq and maxq[-1][0] < y:
            maxq.pop()
        maxq.append((y,i))
        if maxq[0][1] <= i-L: maxq.popleft()

        x,y = minq[0][0],maxq[0][0]
        if x != -1 and i >= L-1:
            result.append((y-x,i-L+1,j-L+1))

print(*sorted(result)[0][1:])
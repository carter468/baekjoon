# 세계일주
# Gold 3, bruteforcing, line intersection

import sys,itertools
input = sys.stdin.readline
INF = sys.maxsize

def travel():
    d = 0
    for i in range(n):
        x1,y1 = arr[p[i]]
        x2,y2 = arr[p[(i+1)%n]]
        d += ((x1-x2)**2+(y1-y2)**2)**0.5
        for j in range(i-1):
            x3,y3 = arr[p[j]]
            x4,y4 = arr[p[j+1]]
            if (x2,y2) == (x3,y3): continue
            if CCW(x1,y1,x2,y2,x3,y3)*CCW(x1,y1,x2,y2,x4,y4) < 0 and CCW(x3,y3,x4,y4,x1,y1)*CCW(x3,y3,x4,y4,x2,y2) < 0:
                return INF
    return d

def CCW(x1,y1,x2,y2,x3,y3):
    return x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

result = INF
for p in itertools.permutations(range(n)):
    result = min(result,travel())
print(result if result != INF else -1)
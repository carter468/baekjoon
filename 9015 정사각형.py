# 정사각형
# Gold 1, 기하학

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    p = set()
    arr = []
    for _ in range(n):
        a,b = map(int,input().split())
        p.add((a,b))
        arr.append((a,b))

    result = 0
    for i in range(n):
        for j in range(n):
            x1,y1,x2,y2 = arr[i]+arr[j]
            if (x1-x2)**2+(y1-y2)**2 <= result: continue
            dx,dy = y1-y2,x1-x2
            if (x1-dx,y1+dy) in p and (x2-dx,y2+dy) in p:
                result = max(result,(x1-x2)**2+(y1-y2)**2)

    print(result)
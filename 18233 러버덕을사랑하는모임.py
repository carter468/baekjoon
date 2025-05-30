# 러버덕을 사랑하는 모임
# Gold 5, bruteforcing, greedy

import itertools

N,P,E = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

for c in itertools.combinations(range(N),P):
    a,b = 0,0
    for i in c:
        a += arr[i][0]
        b += arr[i][1]
    if a <= E <= b:
        result = [0]*N
        t = a
        for i in c:
            x,y = arr[i]
            if t-x+y <= E:
                t = t-x+y
                result[i] = y
            else:
                result[i] = x+E-t
                t = E
        print(*result)
        break
else: print(-1)